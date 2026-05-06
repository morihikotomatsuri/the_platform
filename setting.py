#!/usr/local/bin python3
# setting.py : experimental settings for test

"""
Configuration variables for The Platform simulation.

Variables:
    floors: Number of inhabitants in the experimental building
    experimental_food_range: Range of food amounts to test
    number_of_rounds: Number of simulation rounds per experiment
"""

# Number of floors (inhabitants) in the experimental building
floors = 1000

# Range of food amounts to test (start, stop, step)
experimental_food_range = range(0, 100, 10)

# Number of simulation rounds per experiment
number_of_rounds = 100