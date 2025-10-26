from .operations import Operations
from .error_handling import ErrorHandling

class Calculator:
    def __init__(self):
        self.operations = Operations()
        self.error_handler = ErrorHandling()

    def calculate(self, operation, operand1, operand2):
        try:
            result = self.operations.perform_operation(operation, operand1, operand2)
            return result
        except Exception as e:
            return self.error_handler.handle_error(e)