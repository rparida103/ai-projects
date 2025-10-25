# Auto-generated project
Here's a simple deployment guide for the Random Number Generator (RNG) app, including instructions for setting up the environment, running the application, and executing the tests.

## Deployment Guide for Random Number Generator App

### Prerequisites

1. **Python**: Ensure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **pip**: This should be included with Python installations. It is used to install Python packages.

### Step 1: Clone the Repository

If your code is hosted on a version control system like Git, clone the repository to your local machine. If it's not yet in a repository, create a directory for it.

```bash
git clone <repository-url>
cd RandomNumberGeneratorApp
```

### Step 2: Set Up a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

Since this application does not have external dependencies, you can skip this step. However, if you plan to extend the application in the future, you might want to include dependencies in `requirements.txt` and install them using:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Navigate to the `src` directory and run the application:

```bash
cd src
python main.py
```

Follow the prompts in the command-line interface to generate random numbers.

### Step 5: Run the Tests

To ensure the application is functioning correctly, run the tests using `pytest`. First, make sure you have `pytest` installed:

```bash
pip install pytest
```

Then navigate back to the root directory of the project and run:

```bash
pytest tests/
```

This command will execute all the tests defined in the `tests` directory and report the results.

### Step 6: Future Enhancements

Consider implementing the following enhancements to improve the RNG app:

- **Graphical User Interface (GUI)**: Use libraries like Tkinter or PyQt for a more user-friendly experience.
- **RESTful API**: Implement a web interface using Flask or FastAPI to allow remote access to the RNG functionality.
- **User Preferences**: Store user preferences and history using a database like SQLite.

### Summary

You have successfully deployed the Random Number Generator app. You can now generate random numbers through the command line and run tests to ensure everything is functioning as expected. For further development, consider exploring enhancements that could improve user experience and functionality.