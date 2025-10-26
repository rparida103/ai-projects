from user_interface import UserInterface
from calculator import Calculator
from error_handling import ErrorHandling


def main():
    calculator = Calculator()
    error_handler = ErrorHandling()
    ui = UserInterface(calculator, error_handler)
    ui.start()


if __name__ == '__main__':
    main()