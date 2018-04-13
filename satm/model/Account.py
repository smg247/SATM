


class Account():

    def __init__(self, pan, pin):
        self.pan = pan
        self.pin = pin
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount