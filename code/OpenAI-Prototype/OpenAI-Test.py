import openai
import sqlite3
import sqlparse

def create_openai_client():
    """
    Creates and returns an OpenAI client instance.
    """
    return openai.OpenAI()

def get_database_schema(db_path):
    """
    Retrieves the database schema (tables and their keys) from an SQLite database.

    :param db_path: Path to the SQLite database file.
    :return: A formatted string with table names and their primary keys.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Retrieve table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        schema_info = []
        for table in tables:
            table_name = table[0]
            # Retrieve primary key of the table
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            primary_keys = [col[1] for col in columns if col[5] == 1]
            schema_info.append(f"{table_name} (Primary Key: {', '.join(primary_keys)})")

        conn.close()
        return ', '.join(schema_info)
    except Exception as e:
        return f"Error reading database schema: {e}"

def format_sql_query(raw_sql):
    """
    Formats the raw SQL query for better readability.

    :param raw_sql: The raw SQL query string.
    :return: A formatted SQL query.
    """
        # Remove the prefix ```sql and trailing ```
    if raw_sql.startswith("```sql"):
        raw_sql = raw_sql[6:]  # Remove the first 6 characters (```sql)
    if raw_sql.endswith("```"):
        raw_sql = raw_sql[:-3]  # Remove the last 3 characters (```)

    # Trim leading and trailing whitespaces
    raw_sql = raw_sql.strip()

    # Format the SQL query using sqlparse
    formatted_sql = sqlparse.format(raw_sql, reindent=True, keyword_case='upper')
    return formatted_sql

def generate_sql_from_natural_language(client, model, question, database_schema):
    """
    Generates an SQL statement from a natural language question using OpenAI.
    
    :param client: The OpenAI client instance.
    :param model: The model to be used for generation.
    :param question: The natural language question.
    :param database_schema: The database schema information.
    :return: The generated SQL statement or an error message.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a data analyst. Generate SQL queries from natural language descriptions. Provide only the SQL query in response, without explanations or additional text."},
                {"role": "user", "content": f"Question: {question} Database Schema: {database_schema}"}
            ]
        )
        return response.choices[0].message.content  # Extracting the text content from the response
    except Exception as e:
        return f"An error occurred: {e}"

# Main execution
def main():
    client = create_openai_client()
    MODEL = "gpt-4-1106-preview"
    question = "What is the highest rated song(s)?"
    db_path = "chinook.db"

    database_schema = get_database_schema(db_path)
    raw_sql_statement = generate_sql_from_natural_language(client, MODEL, question, database_schema)
    if isinstance(raw_sql_statement, str):
        formatted_sql_statement = format_sql_query(raw_sql_statement)
        print(formatted_sql_statement)
    else:
        print("No valid SQL query returned.")

if __name__ == "__main__":
    main()
