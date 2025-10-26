import pytest; from calculator.operations import Operations;

def test_operations_add():
    operations = Operations()
    result = operations.perform_operation('add', 1, 2)
    assert result == 3;

def test_operations_subtract():
    operations = Operations()
    result = operations.perform_operation('subtract', 5, 3)
    assert result == 2;

def test_operations_multiply():
    operations = Operations()
    result = operations.perform_operation('multiply', 3, 4)
    assert result == 12;

def test_operations_divide():
    operations = Operations()
    result = operations.perform_operation('divide', 10, 2)
    assert result == 5;

def test_operations_divide_by_zero():
    operations = Operations()
    with pytest.raises(ValueError, match='Division by zero'):
        operations.perform_operation('divide', 10, 0);

def test_operations_invalid_operation():
    operations = Operations()
    with pytest.raises(ValueError, match='Invalid operation'):
        operations.perform_operation('invalid', 10, 2);