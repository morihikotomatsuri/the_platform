#!/usr/local/bin python3
# main.py: run Individual-Based Biological Model

"""
Humanity-Evolution Experiment
    Does the humanity evolve in limited food amount situation?
----------
floor_num int:
experimental_food_range int:
humanity_list list:
humanity_list_replicate list:
each_experiment_result list:
HOLE list:
HOLE_passed list:
"""

import setting
import func
from func import the_platform as pf

pf = func.the_platform()

start = pf.start_time()

floor_num = setting.floors
experimental_food_range = setting.experimental_food_range
number_of_rounds = setting.number_of_rounds

humanity_list = []
humanity_list_replicate = []
each_experiment_result = []

for food_amount in experimental_food_range:
    for new_world in range(number_of_rounds):
        HOLE = pf.set_HOLE(floor_num)
        HOLE_passed = pf.spend_month(HOLE, food_amount, number_of_rounds)

        humanity_list = pf.check_humanity(HOLE_passed)
        humanity_list_replicate = pf.calc_mean_set_list(humanity_list, humanity_list_replicate)
        
        print("food amount:", food_amount, ", round", new_world, "mean_humanity", humanity_list_replicate)
    
    each_experiment_result = pf.calc_mean_set_list(humanity_list_replicate, each_experiment_result)

    print(each_experiment_result)

#pf.plot_dot(each_experiment_result)
pf.plot_hist(each_experiment_result)
pf.end_time(start)

### END ###