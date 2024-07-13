
import random
import statistics

def set_stage():
    """
    """
    stomach_capacity = 1
    eaten_amount = 1

    while check_status_value(stomach_capacity, eaten_amount) == False:
        stomach_capacity = random.random()
        eaten_amount = random.random()
    
    greedy_rate = random.random()

    return stomach_capacity, eaten_amount, greedy_rate

def check_status_value(stomach_capacity, eaten_amount):
    """
    """
    stomach_leftover = stomach_capacity - eaten_amount
    
    if stomach_leftover <= 0:
        return False

def set_stage_value(stage:list):
    """
    """
    stomach_capacity = stage[0]
    eaten_amount = stage[1]
    greedy_rate = stage[2]

    return stomach_capacity, eaten_amount, greedy_rate

def check_stuff_states(
    require_amount:float,

    ):
    """
    """

    if require_amount < 0:
        return True
    else:
        return False

def get_reconstruct_stage_num(stage_num:int):
    """
    """
    new_num_list = random.randint(1, stage_num)

    return new_num_list

def get_mean(target_list:list):
    """
    """
    mean_value = statistics.mean(target_list)

    return mean_value