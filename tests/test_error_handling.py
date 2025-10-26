import pytest; from unittest.mock import patch
from error_handling import ErrorHandling


def test_handle_error():
    error_handler = ErrorHandling()
    with patch('builtins.print') as mock_print:
        error_handler.handle_error(ValueError('Test error'))
        mock_print.assert_called_once_with('Error: Test error')