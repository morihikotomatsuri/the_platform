#!/usr/local/bin python3
# main.py: run Individual-Based Biological Model

"""
Humanity-Evolution Experiment
    Does the humanity evolve in limited food amount situation?
"""
import random

import util
import setting

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

def check_status_value(stomach_capacity:float, eaten_amount:float):
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
    
def feeding(
        stage_max:int,
        stages:tuple,
        food_amount:float
        ):
    """
    """
    alive_stages = []
    for i in range(0,stage_max,1):
        if i < len(stages):
            own_stomach_capacity, own_eaten_amount, own_greedy_rate = set_stage_value(stages[i])
            require_amount = (own_stomach_capacity * own_greedy_rate) - own_eaten_amount

            if not util.check_stuff_states(require_amount):
                food_amount = food_amount - require_amount
            
            if food_amount > 0:
                alive_stages.append(stages[i])
        else:
            pass
    

    return alive_stages


def play_platform(feed_rate:float):
    """
    """
    stage_max = setting.stage_max
    #feed_rate = setting.feed_rate
    round = setting.round

    food_amount = stage_max * feed_rate

    # create initial stage
    stages = []
    for stage in range(0,stage_max,1):
        # set status of stage
        stomach_capacity, eaten_amount, greedy_rate = set_stage()

        # append status of one stage to tuple
        stage_status = (stomach_capacity, eaten_amount, greedy_rate)
        stages.append(stage_status)
    
    # first main process
    alive_stages = feeding(stage_max, stages, food_amount)
    
    # after the second process
    for i in range(1, round,1):
    
        new_stage_num = util.get_reconstruct_stage_num(len(alive_stages))
        new_srages = []
        
        for i in range(0,new_stage_num,1):
            new_srages.append(alive_stages[i])
        
        alive_stages = feeding(stage_max, stages, food_amount)

    # summarize
    stomach_capacity_summary_list = []
    eaten_amount_summary_list = []
    greedy_rate_summary_list = []
    for i in range(0, len(alive_stages),1):
        stomach_capacity, eaten_amount, greedy_rate = set_stage()
        stomach_capacity_summary_list.append(stomach_capacity)
        eaten_amount_summary_list.append(eaten_amount)
        greedy_rate_summary_list.append(greedy_rate)
    
    stomach_capacity_summary_mean = util.get_mean(stomach_capacity_summary_list)
    eaten_amount_summary_mean = util.get_mean(eaten_amount_summary_list)
    greedy_rate_summary_mean = util.get_mean(greedy_rate_summary_list)

    require_amount = (stomach_capacity_summary_mean * greedy_rate_summary_mean) - eaten_amount_summary_mean

    #print(require_amount)
    #print(len(alive_stages))

    return require_amount
