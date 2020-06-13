# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:39:32 2020

@author: Kishan
"""

'''
Find maxium difference between two elements in an array 
'''

def max_diff(a):
    min_sofar = None
    max_diff = None
    i = None
    j = None
    if(len(a) > 1):
        #at least the length of the array should be 2, so that min and max will be computed
        min_sofar = a[0]
        for index in range(1,len(a)):
            if a[index] < min_sofar:
                min_sofar = a[index]
            
            