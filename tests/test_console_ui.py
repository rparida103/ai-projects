import pytest; from ui.console_ui import ConsoleUI; from calculator.calculator import Calculator;
from unittest.mock import patch, MagicMock;

@patch('builtins.input', side_effect=['add', '1', '2'])
@patch('builtins.print')
def test_console_ui_add(mock_print, mock_input):
    ui = ConsoleUI()
    ui.calculator = MagicMock(Calculator)
    ui.calculator.calculate.return_value = 3
    ui.start()
    mock_print.assert_called_with('Result: 3');

@patch('builtins.input', side_effect=['divide', '10', '0'])
@patch('builtins.print')
def test_console_ui_divide_by_zero(mock_print, mock_input):
    ui = ConsoleUI()
    ui.calculator = MagicMock(Calculator)
    ui.calculator.calculate.return_value = 'Division by zero'
    ui.start()
    mock_print.assert_called_with('Result: Division by zero');