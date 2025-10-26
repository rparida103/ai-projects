import pytest; from calculator.calculator import Calculator; from calculator.operations import Operations; from calculator.error_handling import ErrorHandling;

class MockOperations:
    def perform_operation(self, operation, operand1, operand2):
        if operation == 'add':
            return operand1 + operand2
        elif operation == 'subtract':
            return operand1 - operand2
        elif operation == 'multiply':
            return operand1 * operand2
        elif operation == 'divide':
            if operand2 == 0:
                raise ValueError('Division by zero')
            return operand1 / operand2
        else:
            raise ValueError('Invalid operation');

class MockErrorHandling:
    def handle_error(self, error):
        return str(error);

def test_calculator_add():
    calculator = Calculator()
    calculator.operations = MockOperations()
    result = calculator.calculate('add', 1, 2)
    assert result == 3;

def test_calculator_subtract():
    calculator = Calculator()
    calculator.operations = MockOperations()
    result = calculator.calculate('subtract', 5, 3)
    assert result == 2;

def test_calculator_multiply():
    calculator = Calculator()
    calculator.operations = MockOperations()
    result = calculator.calculate('multiply', 3, 4)
    assert result == 12;

def test_calculator_divide():
    calculator = Calculator()
    calculator.operations = MockOperations()
    result = calculator.calculate('divide', 10, 2)
    assert result == 5;

def test_calculator_divide_by_zero():
    calculator = Calculator()
    calculator.operations = MockOperations()
    result = calculator.calculate('divide', 10, 0)
    assert result == 'Division by zero';

def test_calculator_invalid_operation():
    calculator = Calculator()
    calculator.operations = MockOperations()
    result = calculator.calculate('invalid', 10, 2)
    assert result == 'Invalid operation';