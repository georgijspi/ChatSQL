from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory, FileChatMessageHistory
from langchain.prompts import (
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
import sqlite3
from dotenv import load_dotenv

# Ignore deprecation warning from langchain
import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
load_dotenv()

# Create and initialize the OpenAI client
def create_openai_client():
    return ChatOpenAI(model_name="gpt-3.5-turbo-0125")

# Retrieve the database schema from an SQLite database
def get_database_schema(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        schema_info = []
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]  # Fetch only column names
            schema_info.append(f"{table_name}: {', '.join(column_names)}")

        conn.close()
        return '; '.join(schema_info)
    except Exception as e:
        return f"Error reading database schema: {e}"

# Function to execute a SQL query and return results
def execute_sql_query(db_path, sql_query):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        return f"SQL Error: {e}"

class ChatbotProcessor:
    def __init__(self, db_path, model_name="gpt-3.5-turbo-0125", max_token_limit=16385):
        self.db_path = db_path
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

    def get_database_schema(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            schema_info = []
            for table in tables:
                table_name = f'"{table[0]}"'  # Wrap table name in quotes
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns = cursor.fetchall()

                # Wrap column names in quotes
                formatted_column_names = [f'"{col[1]}"' for col in columns]
                schema_info.append(f"{table_name}: {', '.join(formatted_column_names)}")

            conn.close()
            return '; '.join(schema_info)
        except Exception as e:
            return f"Error reading database schema: {e}"



    def execute_sql_query(self, sql_query):
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute(sql_query)
                results = cursor.fetchall()
                conn.close()
                return results
            except sqlite3.Error as e:
                return f"SQL Error: {e}"

    def reset_memory(self):
        print("Chat history cleared.")
        # Clear the chat history
        with open("chat_history.json", "w") as file:
            file.write("[]")

    def process_message(self, question):
        # Load the current conversation history
        current_memory = self.memory.load_memory_variables({})
        history_messages = current_memory.get('history', [])
        print(f'History sent to llm: {history_messages}')

        # Check if the schema has been sent in the current memory buffer
        schema_already_sent = any("Database Schema:" in message.content for message in history_messages)
        database_schema = self.get_database_schema()

        # Define prompt templates with conditional inclusion of database schema
        question_prompt = ChatPromptTemplate(
            input_variables=["history", "question"],
            messages=[
                MessagesPlaceholder(variable_name="history"),
                HumanMessagePromptTemplate.from_template(
                    "\nYou are a data analyst. Generate SQL queries from natural language descriptions. Provide only the SQL query in response, without explanations or additional text." # Keep the column and table names as it and do not add unecessary underscores in column names where there are spaces, in such cases enclose the column name with quotes
                    "Question: {question}\n "
                ),
            ],
        )

        question_chain = LLMChain(
            llm=self.client,
            prompt=question_prompt,
            output_key="sql_query",
            memory = self.memory,
        )

        nlp_prompt = ChatPromptTemplate(
            input_variables=["question", "query_results"],
            messages=[
                HumanMessagePromptTemplate.from_template(
                    "You are a data analyst. Generate a natural language response from the given Question: {question}\nand its SQL output: {query_results}. Provide only the natural language response, without explanations or additional text"
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
            if not schema_already_sent:
                question_result = question_chain(
                    {"question": f"Question: {question}. Database Schema: {database_schema}", "history": history_messages}
                )
            else:
                question_result = question_chain(
                    {"question": f"Question: {question}", "history": history_messages}
                )
            sql_query = question_result["sql_query"]

            print(f'sql_query: {sql_query}')
            # Estimate the token length of the current conversation + SQL query
            current_tokens = estimate_token_length(" ".join([msg.content for msg in history_messages]) + sql_query)

            print(f'current_tokens: {current_tokens}')

            if current_tokens > self.max_token_limit:
                print("Exceeded token limit, skipping this iteration.")
                continue

            query_results = self.execute_sql_query(sql_query)

            print(f'query_results: {query_results}')

            if isinstance(query_results, str) and query_results.startswith("SQL Error"):
                continue
            
            # Check if query_results is an empty list
            if not query_results:
                incorrect_response = "This is incorrect, the data format you are trying may be incorrect."
                self.memory.save_context({"input": incorrect_response}, {"output": "I'll try better"})
                continue

            nlp_result = nlp_chain({"question": question, "query_results": query_results, "history": history_messages})
            bot_response = nlp_result["nlp_response"]

            # Save only successful interaction to the memory
            self.memory.save_context({"input": question}, {"output": bot_response})
            return bot_response

        return "Failed to generate a valid SQL query ;(. This means that the data you are looking for does not exist or you are not giving enough context."

def estimate_token_length(text):
    # Roughly estimate token length for a given text
    return len(text.split())

# Flask route integration
def process_chat_message(question, db_path):
    processor = ChatbotProcessor(db_path)
    return processor.process_message(question)
