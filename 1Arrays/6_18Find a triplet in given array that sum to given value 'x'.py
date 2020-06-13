# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:20:40 2020

@author: Kishan
"""

'''
Problem statement: Find a triplet in given array that sum to given value 'x'

'''

def find_triplet_by_regular_method(inp, sum):
    inp.sort()
    for a in inp:
        for b in inp[1:] :
            c = sum - (a+b)
            if c in inp:
                return a, b, c
            else:
                continue

def find_triplet_partition_method(inp, x):
    inp.sort()
    r = len(inp)
    for i in range(0,r):
        l = i+1
        sum_ = inp[i] + inp[l] + inp[r] 
        if(sum_ == x):
            return inp[i],inp[l],inp[r]
        elif(sum_ > x):
            r -= 1
        elif(sum_ < x):
            l += 1

input_ = list(map(int,input().split()))
a, b, c = find_triplet_by_regular_method(input_,int(input()))
print("{} + {} + {} = {}".format(a,b,c, a+b+c))

print("Approach-2 output")
x, y, z = find_triplet_by_regular_method(input_,int(input()))
print("{} + {} + {} = {}".format(x,y,z, x+y+z))

