import pytest
from utils import format_date
from datetime import datetime


def test_format_date():
    date = datetime(2023, 10, 1)
    assert format_date(date) == '2023-10-01'


def test_string_manipulation_example():
    assert string_manipulation_example('  Hello World  ') == 'hello world'