def add(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    return num1 - num2

def multiply(num1: int, num2: int) -> int:
    return num1 * num2

def divide(num1: int, num2: int) -> int:
    return num1 / num2


class InsufficientFunds(Exception):
    pass
class BankAcc():
    def __init__(self, starting_Balance=0):
        self.balance =  starting_Balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds('Insufficient funds')
            # raise ZeroDivisionError()
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1