from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory, FileChatMessageHistory
from langchain.prompts import (
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
import sqlite3, re, openai
from dotenv import load_dotenv

# Ignore deprecation warning from langchain
import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

load_dotenv()

# Helper function to roughly estimate token length for a given text
def estimate_token_length(text):
    return len(text.split())

# Different models tested:
# gpt-3.5-turbo-0125
# gpt-4-1106-preview

class ChatbotProcessor:
    def __init__(self, db_path, model_name="gpt-4-1106-preview", max_token_limit=16385, allow_db_edit=False):
        self.db_path = db_path
        self.allow_db_edit = allow_db_edit
        print("Chatbot Processor - Allow DB Edit:", self.allow_db_edit)
        self.SQLclient = ChatOpenAI(model_name=model_name, temperature=0.2)
        self.client = ChatOpenAI(model_name=model_name)
        self.memory = ConversationBufferWindowMemory(
            chat_memory=FileChatMessageHistory("chat_history.json"),
            memory_key="history", 
            k=3,
            return_messages=True,
            max_token_limit=max_token_limit,
        )
        self.schema_sent = False
        self.max_token_limit=max_token_limit

    def generate_sample_content(self):
        schema_info = self.get_database_schema()

        description_prompt = ChatPromptTemplate(
            input_variables=["schema_info"],
            messages=[
                HumanMessagePromptTemplate.from_template("Generate the following for a database with the following schema: {schema_info}:\n a title enclosed in a <h1 class='text-gray-700'> tag,\n a detailed 2-3 sentence layman's description of the schema enclosed in a <p class='text-gray-700'> tag,\n and a <h2 class='text-gray-700'> 'Sample Questions:' heading with 3-4 sample questions enclosed in separate newline <p class='text-gray-700'> tags. Do not provide additional text or explanations."),
            ],
        )

        description_chain = LLMChain(
                llm=self.client,
                prompt=description_prompt,
                output_key="schema_description",
            )
        
        try:
            result = description_chain({"schema_info": schema_info})

            return result["schema_description"]
        except Exception as e:
            print(f'Response: {result["schema_description"]}')
            return f"Error in generating content: {e}"

    def get_database_schema(self):
        if not self.db_path:
            raise ValueError("Empty database path provided")

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            full_schema_info = []

            for table in tables:
                table_name = table[0]

                # Fetch schema details
                cursor.execute(f"PRAGMA table_info('{table_name}');")
                columns = cursor.fetchall()
                formatted_columns = [f'"{col[1]}" {col[2]}' for col in columns]
                schema_info = f"Table '{table_name}' with columns: {', '.join(formatted_columns)}."

                # Fetch the first row of data as a sample
                cursor.execute(f"SELECT * FROM '{table_name}' LIMIT 1;")
                sample_data = cursor.fetchone()
                if sample_data:
                    sample_data_info = ', '.join([f'"{col[1]}": {val}' for col, val in zip(columns, sample_data)])
                    sample_data_info = f"Sample data: {{ {sample_data_info} }}"
                else:
                    sample_data_info = "Sample data: None."

                # Combine schema and sample data
                full_table_info = f"{schema_info} {sample_data_info}"
                full_schema_info.append(full_table_info)

            conn.close()
            return ' '.join(full_schema_info)
        except Exception as e:
            return f"Error reading database schema: {e}"

    def execute_sql_query(self, sql_query):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute(sql_query)

            if sql_query.strip().lower().startswith("select"):
                # Fetch results for SELECT queries
                results = cursor.fetchall()
                results_str = ", ".join(map(str, results))
            else:
                # For modification queries like INSERT, UPDATE, DELETE
                conn.commit()
                results_str = "Database update succeeded. Rows affected: " + str(cursor.rowcount)

            conn.close()
            return results_str
        except sqlite3.Error as e:
            return f"SQL Error: {e}"


    def reset_memory(self):
        print("Chat history cleared.")
        self.memory.clear()
        # Clear the chat history
        with open("chat_history.json", "w") as file:
            file.write("[]")

    def _is_within_token_limit(self, history_messages, question):
        current_tokens = estimate_token_length(" ".join([msg.content for msg in history_messages]) + question)
        return current_tokens < self.max_token_limit

    def generate_sql_query(self, question, history_messages, schema_already_sent, database_schema):
        question_prompt = ChatPromptTemplate(
            input_variables=["history", "question"],
            messages=[
                MessagesPlaceholder(variable_name="history"),
                HumanMessagePromptTemplate.from_template(
                    "\nBased on below question and database schema, generate an SQL query for the following question:\n"
                    "Question: {question}\n "
                    "Do not respond with any additional explanations or text."
                ),
            ],
        )

        question_chain = LLMChain(
            llm=self.SQLclient,
            prompt=question_prompt,
            output_key="sql_query",
            memory=self.memory,
        )

        if not schema_already_sent and self._is_within_token_limit(history_messages, question):
            return question_chain(
                {"question": f"Question: {question}.\n Database Schema: {database_schema}.\n SQLQuery:", "history": history_messages}
            )
        else:
            return question_chain(
                {"question": f"Question: {question}", "history": history_messages}
            )

    def generate_nlp_response(self, question, query_results, history_messages):
        nlp_prompt = ChatPromptTemplate(
            input_variables=["history", "question", "query_results"],
            messages=[
                MessagesPlaceholder(variable_name="history"),
                HumanMessagePromptTemplate.from_template(
                    "You are a data analyst. Generate a natural language response from the given Question: {question}\nand subsequent SQL result: {query_results}. If there is a result, always provide an answer with reference to the original question."
                ),
            ],
        )

        nlp_chain = LLMChain(
            llm=self.client,
            prompt=nlp_prompt,
            output_key="nlp_response",
        )

        return nlp_chain({"question": question, "query_results": query_results, "history": history_messages})

    def process_message(self, question):
        try:
            current_memory = self.memory.load_memory_variables({})

            max_attempts = 6
            sql_error = None

            for attempt in range(max_attempts):
                history_messages = current_memory.get('history', [])
                schema_already_sent = any("Database Schema:" in message.content for message in history_messages)
                database_schema = self.get_database_schema()
                print(f'Database Schema: {database_schema}')

                question_result = self.generate_sql_query(question, history_messages, schema_already_sent, database_schema)
                sql_query = question_result["sql_query"]

                print(f"Attempt {attempt + 1}: SQL Query: {sql_query}")
                
                pattern = r"```sql(.*?)```"
                match = re.search(pattern, sql_query, re.DOTALL | re.IGNORECASE)
                if match:
                    sql_query = match.group(1).strip()
                    
                if not sql_query.strip().lower().startswith("select") and not self.allow_db_edit:
                    sql_error = "Database modification not allowed."
                    return sql_error, {"sql_query": sql_query, "sql_output": sql_error}

                query_results = self.execute_sql_query(sql_query)
                
                print(f"Attempt {attempt + 1}: Query Results: {query_results}")

                if not (isinstance(query_results, str) and query_results.startswith("SQL Error")) and query_results:
                    nlp_result = self.generate_nlp_response(question, query_results, history_messages)
                    bot_response = nlp_result["nlp_response"]
                    self.memory.save_context({"input": question}, {"output": bot_response})
                    debug_info = {"sql_query": sql_query, "sql_output": query_results}
                    return bot_response, debug_info

                sql_error = query_results

            bot_response = "Unable to process your request, this information may not be available."
            debug_info = {"sql_query": sql_query, "sql_output": sql_error}
            return bot_response, debug_info

        except Exception as e:
            print(f"Exception in process_message: {e}")
            return "An unexpected error occurred.", {"sql_query": "N/A", "sql_output": "Exception: " + str(e)}
    
# Flask route integration
def process_chat_message(question, db_path):
    processor = ChatbotProcessor(db_path)
    response, debug_info = processor.process_message(question)
    return response, debug_info
