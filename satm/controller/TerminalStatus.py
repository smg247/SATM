from random import *

def is_deposit_slot_functional():
    rand = randint(1, 10)
    return rand > 2 # Give it an 80% chance of being functional
