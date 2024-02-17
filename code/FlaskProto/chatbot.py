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

# gpt-3.5-turbo-0125
# gpt-4-1106-preview

class ChatbotProcessor:
    def __init__(self, db_path, model_name="gpt-3.5-turbo-0125", max_token_limit=16385, allow_db_edit=False):
        self.db_path = db_path
        self.allow_db_edit = allow_db_edit
        print("==Chatbot Processor - Allow DB Edit:", self.allow_db_edit)
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
        # Retrieve the database schema
        schema_info = self.get_database_schema()

        # Prepare a prompt for OpenAI API
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
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            schema_info = []
            sample_data_info = {}
            for table in tables:
                table_name = table[0]

                # Fetch schema details
                cursor.execute(f"PRAGMA table_info('{table_name}');")
                columns = cursor.fetchall()
                formatted_columns = [f'"{col[1]}" {col[2]}' for col in columns]
                schema_info.append(f"{table_name}: {', '.join(formatted_columns)}")

                # Fetch the first row of data as a sample
                cursor.execute(f"SELECT * FROM '{table_name}' LIMIT 1;")
                sample_data = cursor.fetchone()
                sample_data_info[table_name] = dict(zip([col[1] for col in columns], sample_data)) if sample_data else {}

            conn.close()
            return {'schema': '; '.join(schema_info), 'sample_data': sample_data_info}
        except Exception as e:
            return f"Error reading database schema: {e}"

    def execute_sql_query(self, sql_query):
        try:
            # Use regex to extract the SQL query if it's within backticks
            pattern = r"```sql(.*?)```"
            match = re.search(pattern, sql_query, re.DOTALL | re.IGNORECASE)
            if match:
                sql_query = match.group(1).strip()  # Extract the SQL query

            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Check if the query is a SELECT query or if editing is allowed
            if sql_query.strip().lower().startswith("select") or self.allow_db_edit:
                cursor.execute(sql_query)

                if sql_query.strip().lower().startswith("select"):
                    results = cursor.fetchall()  # Fetch results for SELECT queries
                    results = "The result is: " + ", ".join(map(str, results)) # When we execute SQL for SELECT queries
                else:
                    conn.commit()  # Commit changes for non-SELECT queries
                    results = "Database update succeeded. Rows affected: " + str(cursor.rowcount) # When we execute SQL for database modification queries
            else:
                results = []

            conn.close()
            return results
        except sqlite3.Error as e:
            return f"SQL Error: {e}" # For SQL Errors

    def reset_memory(self):
        print("Chat history cleared.")
        # Clear the chat history
        with open("chat_history.json", "w") as file:
            file.write("[]")

    def process_message(self, question):
            # Load the current conversation history
            current_memory = self.memory.load_memory_variables({})
            history_messages = current_memory.get('history', [])

            # Check if the schema has been sent in the current memory buffer
            schema_already_sent = any("Database Schema:" in message.content for message in history_messages)
            database_schema = self.get_database_schema()

            print(database_schema)
            # Define prompt templates
            question_prompt = ChatPromptTemplate(
                input_variables=["history", "question"],
                messages=[
                    MessagesPlaceholder(variable_name="history"),
                    HumanMessagePromptTemplate.from_template(
                        "\nYou are a data analyst. Generate SQL queries from natural language descriptions. Provide only the SQL query in response, without explanations or additional text."
                        "Question: {question}\n "
                    ),
                ],
            )

            question_chain = LLMChain(
                llm=self.client,
                prompt=question_prompt,
                output_key="sql_query",
                memory=self.memory,
            )

            nlp_prompt = ChatPromptTemplate(
                input_variables=["question", "query_results"],
                messages=[
                    HumanMessagePromptTemplate.from_template(
                        "You are a data analyst. Generate a natural language response from the given Question: {question}\nand this additional information: {query_results}. Provide only the natural language response detailing the SQL output that a layman can understand, and minimal additional explanations. If you cannot answer simply say so, with no additional text."
                    ),
                ],
            )

            nlp_chain = LLMChain(
                llm=self.client,
                prompt=nlp_prompt,
                output_key="nlp_response",
            )

            max_retries = 6
            for attempt in range(max_retries):
                try:
                    current_tokens = estimate_token_length(" ".join([msg.content for msg in history_messages]) + question)

                    if not schema_already_sent and current_tokens < self.max_token_limit:
                        question_result = question_chain(
                            {"question": f"Question: {question}. Database Schema: {database_schema}", "history": history_messages}
                        )
                    else:
                        question_result = question_chain(
                            {"question": f"Question: {question}", "history": history_messages}
                        )
                    sql_query = question_result["sql_query"]

                    query_results = self.execute_sql_query(sql_query)

                    if isinstance(query_results, str) and query_results.startswith("SQL Error"):
                        continue

                    if not query_results:
                        incorrect_response = "This is incorrect, the data format you are trying may be incorrect."
                        self.memory.save_context({"input": incorrect_response}, {"output": "I'll try better"})
                        continue

                    nlp_result = nlp_chain({"question": question, "query_results": query_results, "history": history_messages})
                    bot_response = nlp_result["nlp_response"]

                    # Save only successful interaction to the memory
                    self.memory.save_context({"input": question}, {"output": bot_response})
                    return bot_response

                except Exception as e:
                    error_message = str(e)

                    # Check if the error is due to context length
                    if "This model's maximum context length is " in error_message:
                        return "Failed to generate a valid SQL query due to exceeding the maximum context length. Try a different prompt our read our [link]."
                    else:
                        return "An error occurred: " + error_message
                    
            return "Failed to generate a valid SQL query. This means that the data you are looking for does not exist or you are not giving enough context."

# Flask route integration
def process_chat_message(question, db_path):
    processor = ChatbotProcessor(db_path)
    return processor.process_message(question)
