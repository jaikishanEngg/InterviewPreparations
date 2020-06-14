# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:39:48 2020

@author: Kishan
"""

'''
Problem statement:  Given an array of size unknown with all 0's in the beginning and 1's in the end. 
Find the starting index of 1
Solution:
    1. Since we don't know the bounds(size is unknown), we cannot apply binary search
    So, we will start from 0 and increase 2^ till we get a 1
    2. As and when we find a 1, we stop the search.
    we have minimized the array now. In this subarray we know the bounds. 
    so we can apply binary search and find the first index of 1
'''
from math import log, floor, ceil

def linear_search(inp, start_i, end_i):
    try:
        for i in range(start_i, end_i):
            if(inp[i] == 1):
                return i
    except IndexError:
        print("No element 1 found in the array!")
        
def slice_array_atFirstIndex_one(inp):
    '''
    In the unknown size of the binary array, where all the 0's at the left and all the 1's at the end
    As we need to find the first index of 1, as the size is unknown we cannot apply binary search.
    So, we will try to exponentially(2^) increase the step to search for 1 in this function
    While increasing the index step exponentially, it may go beyond the actual size. 
    so handling indexError exception and taking the sub-array by the previous step index and searching linearly
    if exception doesn't raise, then we take the proper sub-array and apply binary search on it to find the first index of 1 in that sub-array
    '''
    try:
        iteration = i =  1
        while(1):
            if(inp[i] == 1):
                #return the upper index with errorstatus False
                return i, False
            else:
                i = 2**iteration
            iteration += 1
    except IndexError:
        #return the upper index with errorstatus True
        return i, True

def binary_search(inp,l_i,h_i):
    '''
    As the all zeros are left and all the ones are at the right - the array is already sorted.
    So binary serach can be applied.
    '''
    m_i = ceil((l_i + h_i)/2)
    if(inp[m_i] == 1 and inp[m_i - 1] != 1):
        return m_i
    elif(inp[m_i] < 1):
        l_i = m_i
        return binary_search(inp,l_i,h_i)
    else:
        h_i = m_i
        return binary_search(inp,l_i,h_i)
    
def find_beginning_one(inp):
    h_i, error_status = slice_array_atFirstIndex_one(inp)
    l_i = floor(2** (int(log(h_i,2)) - 1))
    if(error_status):
        #As the step index raised the error, from the previous step index perform linear search
        return linear_search(inp, l_i, h_i)
    else:
        #As there is no index error, we have got a fixed proper sub-array; so we know the boundaries and can apply binary search
        return binary_search(inp,l_i,h_i)
    

#z = list(map(int,"0 0 0 0 0 0 1 1 1 1 1 1 1 1 1".split()))
z = list(map(int,input().split()))

#print(binary_search(z,0,14))    

print(find_beginning_one(z))
