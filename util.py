
import random

def set_stage():
    """
    """
    stomach_capacity = 1
    eaten_amount = 1
    greedy_rate = 0.5

    stomach_leftover = stomach_capacity - eaten_amount

    while stomach_leftover <= 0:
        stomach_capacity = random.random()
        eaten_amount = random.random()
        
        stomach_leftover = stomach_capacity - eaten_amount
    
    greedy_rate = random.random()

    return stomach_capacity, eaten_amount, greedy_rate

def calc_require_amount(
        stomach_capacity:float,
        greedy_rate:float,
        eaten_amount:float,
    ):
    """
    """

    require_amount = (stomach_capacity * greedy_rate) - eaten_amount

    return require_amount

def check_stuff_states(
    require_amount:float,

    ):
    """
    """

    if require_amount < 0:
        return True
    else:
        return False