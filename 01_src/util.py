
import random
import statistics
import matplotlib
import matplotlib.pyplot

def check_stuff_states(require_amount:float):
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

def create_scatter_plot(target_list:list):
    """
    """
    scatter = matplotlib.pyplot.scatter(range(0, len(target_list), 1), target_list)
    matplotlib.pyplot.show()

    return scatter

def create_histgram(target_list:list, bins:int):
    """
    """
    hist = matplotlib.pyplot.hist(target_list, bins = bins)
    matplotlib.pyplot.show()

    return hist

