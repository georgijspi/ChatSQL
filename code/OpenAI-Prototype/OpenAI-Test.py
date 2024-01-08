import openai

def text_to_sql(question, tables, openai_key):
    """
    Converts an English question to an SQL statement using OpenAI's API.
    
    :param question: The English question to convert.
    :param tables: List of relevant database tables.
    :param openai_key: Your OpenAI API key.
    :return: The generated SQL statement.
    """
    openai.api_key = openai_key

    prompt = f"Given the following English question and database context, please generate an SQL statement:\n\nQuestion: {question}\nDatabase Tables: {tables}"

    try:
        response = openai.Completion.create(
            model="gpt-4-1106-preview",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Replace 'YOUR_OPENAI_KEY' with your actual OpenAI API key
openai_key = 'YOUR_OPENAI_KEY'

# Example usage
question = "How many orders were placed in 2021?"
tables = "orders"
sql_query = text_to_sql(question, tables, openai_key)
print(sql_query)
