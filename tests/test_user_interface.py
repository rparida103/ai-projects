import pytest; from unittest.mock import patch, MagicMock
from user_interface import UserInterface
from calculator import Calculator
from error_handling import ErrorHandling


def test_process_input_valid():
    calculator = Calculator()
    error_handler = ErrorHandling()
    ui = UserInterface(calculator, error_handler)
    with patch('builtins.print') as mock_print:
        ui.process_input('5 + 3')
        mock_print.assert_called_once_with('Result: 8')


def test_process_input_invalid_format():
    calculator = Calculator()
    error_handler = ErrorHandling()
    ui = UserInterface(calculator, error_handler)
    with patch('builtins.print') as mock_print:
        ui.process_input('5 +')
        mock_print.assert_called_once_with('Error: Invalid input format. Use: <number> <operator> <number>')


def test_process_input_unknown_operator():
    calculator = Calculator()
    error_handler = ErrorHandling()
    ui = UserInterface(calculator, error_handler)
    with patch('builtins.print') as mock_print:
        ui.process_input('5 ^ 3')
        mock_print.assert_called_once_with('Error: Unknown operator')