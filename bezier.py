# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:39:44 2016

@author: Calvin
"""
import matplotlib.pyplot as plt
import random
def get_points(use, alpha_step):
    final = []
    for i in range(alpha_step):
        i *= (1.0/(alpha_step-1))
        points = list(use)
        while len(points) != 1: #Ends when there is only one point
            for index, val in enumerate(points[:-1]):
                points[index] = [val[0]+(i*-(val[0]-points[index+1][0])), val[1]+(i*-(val[1]-points[index+1][1]))]
            points.pop(-1)
        final.append(points[0])
    return final
        
use = []      
for i in range(1000):
    use.append([random.randint(-100,100), random.randint(-100,100)]) #Generates random starting points
alpha_step = 1000
final = get_points(use, alpha_step)
plt.plot([use[i][0] for i in range(len(use))], [use[i][1] for i in range(len(use))]) #COMMENT TO HIDE INITIAL POINTS
plt.plot([final[i][0] for i in range(len(final))], [final[i][1] for i in range(len(final))]) #ACTUAL CURVE