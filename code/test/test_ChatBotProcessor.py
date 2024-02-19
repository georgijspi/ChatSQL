import pytest
import sys
sys.path.append('/home/cheezyhint/2024-ca326-cchoa-3yp/code/FlaskProto')
from chatbot import ChatbotProcessor

# Set the OPENAI_API_KEY environment variable for testing
#os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# # Define a fixture to create an instance of ChatbotProcessor
# @pytest.fixture(scope="module")
# def chatbot_processor():
#     # Provide a sample database path for testing
#     db_path = "test1.db"
#     processor = ChatbotProcessor(db_path)
#     return processor

# Test case for successful retrieval of schema
def test_get_database_schema_success():
    db_path = "test1.db"
    processor = ChatbotProcessor(db_path)
    schema = processor.get_database_schema()
    expected_schema = {
        'sample_data': {'test_table': {}},
        'schema': 'test_table: "id" INTEGER, "name" TEXT'
    }
    assert schema == expected_schema


# Test case for error handling - database connection error
def test_get_database_schema_empty_path():
    with pytest.raises(ValueError) as e:
        db_path = ""
        processor = ChatbotProcessor(db_path)
        schema = processor.get_database_schema()
    assert str(e.value) == "Empty database path provided"

# Test case for process_message method
def test_process_message():
    # Test the process_message method with a sample question
    db_path = "test1.db"
    processor = ChatbotProcessor(db_path)
    question = "What is the total sales for this month?"
    response = processor.process_message(question)
    # Assert that the response is not empty
    assert response is not None
    # Add more assertions based on the expected behavior of the process_message method
