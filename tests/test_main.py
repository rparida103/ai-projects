import pytest; from main import main
from unittest.mock import patch


def test_main():
    with patch('builtins.input', side_effect=['5 + 3', 'exit']), patch('builtins.print') as mock_print:
        main()
        mock_print.assert_any_call('Result: 8')