class UserInterface:
    def __init__(self, calculator, error_handler):
        self.calculator = calculator
        self.error_handler = error_handler

    def start(self):
        while True:
            user_input = input('Enter calculation (or type "exit" to quit): ')
            if user_input.lower() == 'exit':
                break
            self.process_input(user_input)

    def process_input(self, user_input):
        try:
            result = self.evaluate_expression(user_input)
            print(f'Result: {result}')
        except Exception as e:
            self.error_handler.handle_error(e)

    def evaluate_expression(self, expression):
        tokens = expression.split()
        if len(tokens) != 3:
            raise ValueError('Invalid input format. Use: <number> <operator> <number>')
        a, operator, b = tokens
        a, b = float(a), float(b)

        if operator == '+':
            return self.calculator.add(a, b)
        elif operator == '-':
            return self.calculator.subtract(a, b)
        elif operator == '*':
            return self.calculator.multiply(a, b)
        elif operator == '/':
            return self.calculator.divide(a, b)
        else:
            raise ValueError('Unknown operator')