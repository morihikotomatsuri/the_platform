#!/usr/local/bin python3
# main.py: run Individual-Based Biological Model

"""
Humanity-Evolution Experiment
    Does the humanity evolve in limited food amount situation?
"""

import util

    
def feeding(
        ):
    """
    """

    
    return leftover

if __name__ == '__main__':
    stage_num = 10
    feed_rate = 1
    round = 10

    # set status of stage
    stomach_capacity, eaten_amount, greedy_rate = util.set_stage()

    food_amount = stage_num * feed_rate

    require_amount = util.calc_require_amount(stomach_capacity,greedy_rate,eaten_amount)

    if not util.check_stuff_states:
        food_amount = food_amount - require_amount

    print(food_amount)
    
    #for i in round - 1:
