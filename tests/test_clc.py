from calculations import add, subtract, multiply, divide, BankAcc, InsufficientFunds
import pytest


@pytest.fixture
def zero_bank_acc():
    return BankAcc()

@pytest.fixture
def bank_acc():
    return BankAcc(50)

# @pytest.mark.parametrize("num1, num2, expected", [
#     (3, 2, 5),
#     (1, 2 ,3),
#     (12, 4, 16)
# ])

# def test_add(num1, num2, expected):
#     print('test_add')
#     assert add(num1, num2) ==expected

# def test_subtract():
#     print('test_subtract')
#     assert subtract(2, 1) == 1
#
# def test_multiply():
#     print('test_multiply')
#     assert multiply(1, 2) == 2
#
# def test_divide():
#     print('test_divide')
#     assert divide(3, 3) == 1

def test_bank_set_initial():
    bank_acc = BankAcc(50)
    assert bank_acc.balance == 50

def test_bank_default_amount(zero_bank_acc):
    # bank_acc = BankAcc()
    assert zero_bank_acc.balance == 0

def test_withdraw():
    bank_acc = BankAcc(50)
    bank_acc.withdraw(20)
    assert bank_acc.balance == 30

def test_deposit():
    bank_acc = BankAcc(50)
    bank_acc.deposit(30)
    assert bank_acc.balance == 80

def test_collect_interest():
    bank_acc = BankAcc(50)
    bank_acc.collect_interest()
    assert round(bank_acc.balance, 6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [ (200, 100, 100), (10, 10, 0)])

def test_bank_transaction(zero_bank_acc, deposited, withdrew, expected):
    zero_bank_acc.deposit(deposited)
    zero_bank_acc.withdraw(withdrew)
    assert zero_bank_acc.balance == expected

def test_insufficient_funds(bank_acc):
    with pytest.raises(InsufficientFunds):
        bank_acc.withdraw(51)
