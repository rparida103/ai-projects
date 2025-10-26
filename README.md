# Auto-generated project
# Deployment Guide for Calculator Application

This guide provides step-by-step instructions for setting up the environment, installing dependencies, running unit tests, and executing the main application for the calculator project.

## 1. Setting Up the Environment

### Step 1: Install Python

Ensure that you have Python 3.7 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. You can create a virtual environment using the following commands:

```bash
# Navigate to the project directory
cd path/to/calculator_app

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## 2. Listing Dependencies

### Step 1: Install Dependencies

The project does not specify any dependencies in the `requirements.txt` file. However, since the project uses `pytest` for testing, you should install it manually. You can do this by running:

```bash
pip install pytest
```

If there are any additional dependencies required in the future, they should be added to the `requirements.txt` file.

## 3. Instructions for Running Unit Tests

To ensure that the application works as expected, you should run the unit tests provided in the `tests` directory. Use the following command:

```bash
pytest
```

This command will automatically discover and run all the test files prefixed with `test_` in the `tests` directory.

## 4. Instructions for Running the Main Application

To run the main application, execute the following command:

```bash
python main.py
```

This will start the calculator application. You can then enter calculations in the format `<number> <operator> <number>` (e.g., `5 + 3`). Type `exit` to quit the application.

## Summary

By following these steps, you will have a fully functional environment for the calculator application, allowing you to run tests and execute the application seamlessly. If you encounter any issues, ensure that your Python installation and virtual environment setup are correct.