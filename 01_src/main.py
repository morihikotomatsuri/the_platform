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

    # change feed_rate 0.1-1.0
    result_replicate=[]
    for i in range(1, 100, 1):
        # run platform func a set number of replicates
        result = []
        for j in range(1, setting.replicate, 1):
            feed_rate = i * 0.01
            require_amount = the_platform.play_platform(feed_rate)
            result.append(require_amount)
            result_mean = util.get_mean(result)
        result_replicate.append(result_mean)
        print("feed_rate = " + str(feed_rate))
    
    # create summary plot
    scatter = util.create_scatter_plot(result_replicate)
    hist = util.create_histgram(result_replicate, 30)

    ### END ###

    


