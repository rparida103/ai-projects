from calculator.calculator import Calculator

class ConsoleUI:
    def __init__(self):
        self.calculator = Calculator()

    def start(self):
        while True:
            operation = input('Enter operation (add, subtract, multiply, divide) or type exit to quit: ')
            if operation == 'exit':
                break
            operand1 = float(input('Enter first operand: '))
            operand2 = float(input('Enter second operand: '))
            result = self.calculator.calculate(operation, operand1, operand2)
            print(f'Result: {result}')