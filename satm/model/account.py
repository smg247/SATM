class Account():

    def __init__(self, pan, pin):
        self.pan = str(pan)
        self.pin = str(pin)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount