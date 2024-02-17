import pytest
import sys
sys.path.append('/home/cheezyhint/2024-ca326-cchoa-3yp/code/FlaskProto')
from chatbot import get_database_schema


# Test case for successful retrieval of schema
def test_get_database_schema_success():
    schema = get_database_schema("test1.db")
    assert schema == "test_table: id, name"

# Test case for error handling - database connection error
def test_get_database_schema_empty_path():
    with pytest.raises(Exception) as e:
        # Test the function with a empty path
        schema = get_database_schema()

# # Test case for error handling - database connection error
# def test_get_database_schema_non_existing_database_path():
#     with pytest.raises(Exception) as e:
#         # Test the function with a non-existing database path
#         schema = get_database_schema("non_existing.db")