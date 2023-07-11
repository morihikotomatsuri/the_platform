#!/usr/local/bin python3
# func.py : functions of Individual-Based Biological Model

"""
functions:
    class universalFunc()
        get_parameters_from_list(list, element_num)
        plot_hist(list)
        plot_dot(list)
        culc_mean(list)
        start_time()
        end_time(start)
        calc_mean_set_list(list, new_list)
    class the_platform(universalFunc)
        set_initialize_variant(floor,food)
        set_person_parameters()
        set_HOLE(floor_num)
        get_parameters_from_list(list, element_num)
        get_parameters(hole)
        lunchtime(hole, lunch)
        replenish_surviver(hole)
        check_humanity(hole)
        plot_hist(list)
        plot_line(list)
        wake_up(list)
        culc_mean(list)
        start_time()
        end_time(start)
        spend_month(hole, food_amount, times)
        calc_mean_set_list(list, new_list)
"""

from os import remove
import random
from statistics import mean
import matplotlib.pyplot as plt
import random
import time

class universalFunc():
    def recommend(self):
        print("")

    def get_parameters_from_list(self, list, element_num):
        """
        Args:
        Return:
            element *

        -----
        element *:
            element is sth indicated by element_num in list.
        """

        element = list[element_num]

        return element

    def plot_hist(list):
        """
        Args:
            list list:
                list is the numbers to plot histgram.
        Return:
            none
        ---------
        """

        plt.xlim(0.1, 0.5) 
        plt.hist(list)
        plt.show()

        return

    def plot_dot(list):
        """
        Args:
            list list:
                list is the numbers to plot histgram.
        Return:
            none
        ---------
        """

        plt.plot(list, "bo")
        plt.show()

        return

    def culc_mean(self, list):
        """
        Args:
            list list:
                list is the target to shuffle.
        Return:
            mean_nim float:
                mean_num is the mean number of input list.
        ----------
        mean_nim float:
            mean_num is the mean number of input list.
        """

        mean_num = mean(list)

        return mean_num

    def calc_mean_set_list(self, list, new_list):
        """
        Args:
            list list:
                list is the target list, not dict.
            new_list list:
                new_list is the result append list.
        Return:
            new_list list:
        ----------
        new_list list:
            new_list is the result append list.
        mean int:
            mean is the result of calculate.
        """

        new_list = []
        mean = self.culc_mean(list)
        new_list.append(mean)

        return new_list

    def start_time(self):
        """
        Args:
        Return:
        ----------
        start float:
            start is the time stamp indicating start time.
        """

        start = time.time()

        return start

    def end_time(self,start):
        """
        Args:
            start float:
                start is the time stamp indicating start time.
        Return:
        ----------
        elapsed_time float:
            elapsed_time is the time stamp indicating the end.
        """

        elapsed_time = time.time() - start
        print(elapsed_time/3600/24, "days")

        return

class the_platform(universalFunc):
    def recommend(self):
        print("")

    def set_initialize_variant(floor,food):
        """
        Args:
            floor int:
                floor is the size of HOLE floors. 
            food int:
                food is the initial food amount.
        Result:
        ----------
        """

        return floor,food

    def set_person_parameters(self):
        """
        Args:
        Returns:
            person list
        -----
        food_require float:
            food_require is the amount of required food amount.
        food_greedy float:
            food_greedy is the amount of extra food amount to be full.
        servive_flag bool:
            servive_flag is the index of human life (dead or alive).
        person list:
            person is the list include parameters above.
        """

        food_require = random.random()
        food_greedy = random.uniform(food_require, 1)
        servive_flag = True

        person = [food_require, food_greedy, servive_flag]

        return person

    def set_HOLE(self,hole_depth):
        """
        Args:
            hole_depth float:
                hole_depth is the size of HOLE list. 
        Returns:
            HOLE list
        -----
        HOLE list:
            HOLE is the experimental building for THE PLATFORM.
        man list:
            man is the list include parameters named food_require and food_greedy in set_person_parameters.
        """

        HOLE=[]
        for i in range(hole_depth):
            man = self.set_person_parameters()
            HOLE.append(man)
        
        return HOLE

    def get_parameters(hole):
        """
        Args:
            hole list:
                hole is the experimental building for THE PLATFORM.
        Return:
            patiant_food_require_list float
            patiant_food_greedy_list float
        -----
        patiant_food_require_list list:
            patiant_food_require is the list of required food amount.
        patiant_food_greedy_list list:
            patiant_food_greedy is the list of extra food amount to be full.
        hole_depth int:
            hole_depth is the floor number of THE HOLE.
        floor int:
            floor is the target floor number.
        patiant list:
            patiant is the list housed in the HOLE
        patiant_food_require float:
            patiant_food_require is the amount of required food amount.
        patiant_food_greedy float:
            patiant_food_greedy is the amount of extra food amount to be full.

        """

        patiant_food_require_list = []
        patiant_food_greedy_list = []
        hole_depth = len(hole)

        for floor in range(hole_depth):
            patiant = hole[floor]
            patiant_food_require = self.get_parameters_from_list(patiant, 0)
            patiant_food_greedy = self.get_parameters_from_list(patiant, 1)

            patiant_food_require_list.append(patiant_food_require)
            patiant_food_greedy_list.append(patiant_food_greedy)

        return patiant_food_require_list, patiant_food_greedy_list

    def lunchtime(self, hole, lunch):
        """
        Args:
            hole list:
                hole is the experimental building for THE PLATFORM.
            lunch float:
                lunch is the food amount to serve to the HOLE.
        Return:
            hole list:
                hole is the experimental building for THE PLATFORM.
        -----
        last_lunch float:
            last_lunch is the last food amount after served to each floor.
        floor int:
            floor is the target floor number.
        hole_depth int:
            hole_depth is the size of the HOLE.
        patiant list:
            patiant is the list housed in the HOLE.
        patiant_food_require float:
            patiant_food_require is the amount of required food amount.
        patiant_food_greedy float:
            patiant_food_greedy is the amount of extra food amount to be full.
        """

        last_lunch = lunch
        hole_depth = len(hole)

        for floor in range(hole_depth):
            patiant = hole[floor]
            patiant_food_require = self.get_parameters_from_list(patiant, 0)
            patiant_food_greedy = self.get_parameters_from_list(patiant, 1)

            if patiant_food_greedy <= last_lunch:
                last_lunch -= patiant_food_greedy
            elif patiant_food_require <= last_lunch:
                last_lunch -= patiant_food_require
            else:
                last_lunch = 0
                patiant[2] = 0
        
            if last_lunch < 0:
                last_lunch = 0
        
        return hole

    def replenish_surviver(self, hole):
        """
        Args:        
            hole list:
                hole is the experimental building for THE PLATFORM.
        Return:
            hole list:
                hole is the result of the lunchtime.
        -----
        floor int:
            floor is the target floor number.
        hole_depth int:
            hole_depth is the size of the HOLE.
        patiant list:
            patiant is the list housed in the HOLE
        man list:
            man is the list include parameters in set_person_parameters.
        """

        hole_depth = len(hole)

        for floor in range(hole_depth):
            patiant = hole[floor]
            
            if patiant[2] == 0:
                man = self.set_person_parameters()
                hole[floor] = man

        return hole

    def check_humanity(self, hole):
        """
        Args:
            hole list:
                hole is the experimental building for THE PLATFORM.
        Return:
        humanity_list list:
            humanity_list is the result of the experiment.
        ----------
        hole_depth int:
            hole_depth is the size of the HOLE.
        humanity_list list:
            humanity_list is the result of the experiment.
        require float:
            require is the amount of required food amount.
        greedy float:
            greedy is the amount of extra food amount to be full.
        """

        humanity_list = []
        hole_depth = len(hole)

        for floor in range(hole_depth):
            patiant = hole[floor]
            require = patiant[0]
            greedy = patiant[1]

            humanity = greedy - require
            humanity_list.append(humanity)

        return humanity_list
        
    def plot_hist(self, list):
        """
        Args:
            list list:
                list is the numbers to plot histgram.
        Return:
            none
        ---------
        """

        plt.xlim(0, 1) 
        plt.hist(list)
        plt.show()

        return

    def plot_dot(self, list):
        """
        Args:
            list list:
                list is the numbers to plot histgram.
        Return:
            none
        ---------
        """

        plt.plot(list, "bo")
        plt.show()

        return

    def wake_up(self, list):
        """
        Args:
            list list:
                list is the target to shuffle.
        Return:
            list list:
                list is the shuffled target.
        ----------
        """

        random.shuffle(list)

        return list

    def spend_month(self, hole, food_amount, times):
        """
        Args:
            hole list:
                hole is the experimental building for THE PLATFORM.
            food_amount int:
                food_amount is the served food amount.
            times int:
                times is the number of rounds.
        Return:
            hole list:
        ----------
        """

        for i in range(times):
            hole = self.lunchtime(hole, food_amount)
            hole = self.replenish_surviver(hole)
            hole = self.wake_up(hole)
        
        return hole
    
    def start_time(self):
        """
        Args:
        Return:
        ----------
        start float:
            start is the time stamp indicating start time.
        """

        start = time.time()

        return start