# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:58:22 2020

@author: Kishan
"""
'''
Problem statement: Separate 0's and 1's in an array 

Solutions:
    1. Couting sort:
        Use hash table contains 0 and 1 as keys, its values as thier count in the array
    2. Partition algorithm used in Quick sort:
'''

def counting_sort(inp):
    hash_m = dict()
    output = []
    
    #iterate through the input and maintain the count of 0's and 1's
    for i in inp:
        if i in hash_m:
            hash_m[i] += 1
        else:
            hash_m[i] = 1
    
    #create a output list with the seperate count of 0's and 1's together
    
    for k,v in hash_m.items():
        output += [k]*v
    
    return output

def partitioning_alg(inp):
    l = 0
    r = len(inp) - 1 #last index
    while(l < r):
        while(inp[l]==0 and l<r):
            l += 1
        while(inp[r]==1 and r>l):
            r -= 1
        if(l<r):
            #swap
            inp[l], inp[r] = inp[r], inp[l]
    return inp

print(partitioning_alg([0,1,1,0,1,1,0]))
