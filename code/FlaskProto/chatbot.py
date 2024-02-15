from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryBufferMemory, ChatMessageHistory
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
        return '; '.join(schema_info)  # Use a semi-colon to separate each table's schema
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

# Save chat history to a JSON file
# memory = ConversationBufferMemory(
#     chat_memory=FileChatMessageHistory("chat_history.json"),
#     memory_key="messages",
#     return_messages=True,
# )

class ChatbotProcessor:
    def __init__(self, db_path, model_name="gpt-3.5-turbo-0125", max_token_limit=16385):
        self.db_path = db_path
        self.client = ChatOpenAI(model_name=model_name)
        self.memory = ConversationSummaryBufferMemory(llm=self.client, 
                                                    max_token_limit=max_token_limit,
                                                    memory_key="history",
                                                    return_messages=True,
                                                    )

    def get_database_schema(self):
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()

                schema_info = []
                for table in tables:
                    table_name = table[0]
                    cursor.execute(f"PRAGMA table_info({table_name});")
                    columns = cursor.fetchall()
                    column_names = [col[1] for col in columns]
                    schema_info.append(f"{table_name}: {', '.join(column_names)}")

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

    def process_message(self, question):
        
        database_schema = self.get_database_schema()

        # Define prompt templates
        question_prompt = ChatPromptTemplate(
            input_variables=["history", "question"],
            messages=[
                HumanMessagePromptTemplate.from_template(
                    "{history}\nYou are a data analyst. Generate SQL queries from natural language descriptions. Provide only the SQL query in response, without explanations or additional text"
                    "Question: {question}Response: "
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
            question_result = question_chain(
                {"question": f"Question: {question}\nDatabase Schema: {database_schema}"}
            )
            sql_query = question_result["sql_query"]
            query_results = self.execute_sql_query(sql_query)

            if isinstance(query_results, str) and query_results.startswith("SQL Error"):
                continue

            nlp_result = nlp_chain({"question": question, "query_results": query_results})
            return nlp_result["nlp_response"]

        return "Failed to generate a valid SQL query after maximum retries."

# Flask route integration
def process_chat_message(question, db_path):
    processor = ChatbotProcessor(db_path)
    return processor.process_message(question)
