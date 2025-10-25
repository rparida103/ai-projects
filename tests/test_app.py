To write unit tests for the provided Flask application using `pytest`, we need to create a test file that will cover the functionality of the API endpoints defined in the application. Below is an example of how to set up the tests, including the necessary fixtures to create a test client and a test database.

### Test Structure

1. **Create a test directory**
```
/user-input-app
├── /tests
│   └── test_input.py
```

2. **Test File (`/tests/test_input.py`)**

```python
import pytest
from flask import Flask
from backend.app import app
from backend.database.db import db
from backend.models.input import UserInput

@pytest.fixture(scope='module')
def test_client():
    # Create a test Flask application
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # Create tables
        yield app.test_client()  # Provide the test client
        db.drop_all()  # Clean up after tests

def test_create_input(test_client):
    # Test creating a new user input
    response = test_client.post('/api/inputs', json={
        'input_type': 'text',
        'input_value': 'Hello World'
    })
    assert response.status_code == 201
    assert response.get_json() == {"message": "Input captured successfully!"}

    # Check if the input was added to the database
    input_record = UserInput.query.first()
    assert input_record is not None
    assert input_record.input_type == 'text'
    assert input_record.input_value == 'Hello World'

def test_create_input_invalid(test_client):
    # Test creating a new user input with missing fields
    response = test_client.post('/api/inputs', json={
        'input_type': 'text'
    })
    assert response.status_code == 400
    assert 'input_value' in response.get_json()

def test_get_inputs(test_client):
    # Test retrieving inputs
    response = test_client.get('/api/inputs')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)  # Should return a list

    # Add an input and test again
    test_client.post('/api/inputs', json={
        'input_type': 'text',
        'input_value': 'Another input'
    })
    response = test_client.get('/api/inputs')
    assert response.status_code == 200
    inputs = response.get_json()
    assert len(inputs) == 1  # Should have one input
    assert inputs[0]['input_value'] == 'Another input'

def test_get_inputs_empty(test_client):
    # Test retrieving inputs when the database is empty
    response = test_client.get('/api/inputs')
    assert response.status_code == 200
    assert response.get_json() == []  # Should return an empty list
```

### Explanation of Tests

1. **Fixtures**: 
   - The `test_client` fixture sets up a test Flask application with an in-memory SQLite database. It creates the database tables before tests and drops them afterward.

2. **Tests**:
   - `test_create_input`: Tests the creation of a new user input and checks if it was successfully added to the database.
   - `test_create_input_invalid`: Tests the creation of a user input with missing fields to ensure proper validation and error handling.
   - `test_get_inputs`: Tests the retrieval of inputs from the database after adding a new input.
   - `test_get_inputs_empty`: Tests the retrieval of inputs when the database is empty.

### Running the Tests

To run the tests, navigate to the root of your project directory and execute:

```bash
pytest tests/
```

This will discover and run all the tests in the `tests` directory. Make sure you have `pytest` installed in your environment. If not, you can install it using:

```bash
pip install pytest
```

This setup will help ensure that your API endpoints are functioning as expected and that the data validation is working correctly.