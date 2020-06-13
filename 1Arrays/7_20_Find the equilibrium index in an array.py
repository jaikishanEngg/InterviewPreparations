# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:39:00 2020

@author: Kishan
"""

'''
Problem statement: Find the equilibrium index in an array
equilibrium index means -- the sum of elements till that index = the sum of the rest elements
'''
from math import floor

def equilibrium_index(inp):
    left_sum = []
    left_sum.append(inp[0])
    #right_sum = []

    for i in range(1,len(inp)):
        left_sum.append(left_sum[i-1] + inp[i])
    
    sum_end = floor(left_sum[-1]/2)
    
    #Find the index which results into half value of the total sum
    for v in range(0,len(left_sum)):
        if(left_sum[v] == sum_end):
            return v
    else:
        return -1

input_ = list(map(int,input().split())) #10 5 15 3 4 21 2

output = equilibrium_index(input_)
if(output == -1):
    print("No Equilibrium point found!")
else:
    print("Equilibrium index: {}".format(output))

#for i in range(1,len(inp)):
#    left_sum.append(left_sum[i-1] + inp[i])
#    
#-10  5  -2  15 10   4 -6   9  11
#
#-10 -5 -7   8  18  22  16  25 36
#
#36  46 41  43 28  18  14  20  11
