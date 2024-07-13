#!/usr/local/bin python3
# main.py

"""
Humanity-Evolution Experiment
    Does the humanity evolve in limited food amount situation?
"""

import the_platform
import util
import setting

if __name__ == '__main__':

    result = []
    for i in range(1, setting.replicate, 1):
        require_amount = the_platform.play_platform()
        result.append(require_amount)
    
    
    result_mean = util.get_mean(result)
    print(result_mean)
    
    scatter = util.create_scatter_plot(result)
    hist = util.create_histgram(result, 100)

    


