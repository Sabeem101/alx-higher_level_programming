#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    weight_score = sum(z[0] * z[1] for z in my_list)
    weight = sum(x[1] for x in my_list)
    return weight_score / weight
