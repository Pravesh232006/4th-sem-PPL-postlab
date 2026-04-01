import time
from logger import log_transaction

class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance   # encapsulated
        self.__pin = pin           # encapsulated

    def check_pin(self, pin):
        return self.__pin == pin

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)
        log_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
            log_transaction("Withdraw", amount)
        else:
            print("Insufficient balance")

    def transfer(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Transferred:", amount)
            log_transaction("Transfer", amount)
        else:
            print("Insufficient balance")