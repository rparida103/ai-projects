import pytest; from calculator.error_handling import ErrorHandling;

def test_handle_error():
    error_handler = ErrorHandling()
    result = error_handler.handle_error(ValueError('Test error'))
    assert result == 'Test error';