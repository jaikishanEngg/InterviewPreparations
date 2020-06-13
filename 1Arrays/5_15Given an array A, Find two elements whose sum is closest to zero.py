# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:55:25 2020

@author: Kishan
"""

'''
Problem statement: Given an array A, Find two elements whose sum is closest to zero
Solution:
    1. sort the array
    2. maintain left and right pointers, 
        if the sum of array[left_i] and array[right_i] is +ve num:
            that means there could be another small number which brings the sum close to zero
            so, reduce the right pointer
        if the sum of array[left_i] and array[right_i] is -ve num:
            that means there could be another big number which may bring the sum close to zero
            so, increase the left pointer
'''

def find_two_num_closeToZero(inp):
    l = 0
    r = len(inp) - 1

    closest_sum = max(inp)

    while(l < r):
        curr_sum = inp[l] + inp[r]
        if(abs(curr_sum) < abs(closest_sum)):
            closest_sum = curr_sum
            min_r_index = r
            min_l_index = l
        
        if(curr_sum > 0):
            r -= 1
        else:
            l += 1
        
    return min_l_index, min_r_index

input_ = sorted(list(map(int,input().split()))) #-2 9 6 1 3 -5 #-2 9 6 1 2 -5
x, y = find_two_num_closeToZero(input_)

print("Elements whose sum close to Zero =  {}+ {} = {}".format(input_[x],input_[y],input_[x]+input_[y] ))