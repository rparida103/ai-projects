class Operations:
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
            raise ValueError('Invalid operation')