import pytest
import json
import sys
sys.path.append('../FlaskProto')
from chatbot import ChatbotProcessor

# Load test data from test_data.json
with open("test_data.json", "r") as file:
    test_data = json.load(file)

# Define a fixture to create an instance of ChatbotProcessor
@pytest.fixture(scope="module")
def chatbot_processor():
    db_path = test_data["database_path"]
    processor = ChatbotProcessor(db_path)
    return processor

# Parametrize test cases for each question-answer pair
@pytest.mark.parametrize("test_case", test_data["tests"])
def test_question_answer_pair(test_case, chatbot_processor):
    question = test_case["question"]
    expected_result = test_case["expected_sql_result"]
    database_schema = chatbot_processor.get_database_schema()
    question_result = chatbot_processor.generate_sql_query(question, [], False, database_schema)
    sql_query = question_result["sql_query"]
    response = chatbot_processor.execute_sql_query(sql_query)
    assert response == expected_result
