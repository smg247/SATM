from random import *

def is_deposit_slot_functional():
    rand = randint(1, 10)
    return rand > 2 # Give it an 80% chance of being functional


def is_withdrawal_slot_functional():
    rand = randint(1, 10)
    return rand > 3  # Give it an 70% chance of being functional


def total_currency():
    return randint(50, 200)