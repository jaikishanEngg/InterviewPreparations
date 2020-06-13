# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:26:38 2020

@author: Kishan
"""

'''
1Interview Preparation- Find a pair in an array whose sum is equal to given number (Hash Approach)

Problem statement: Given an array A and a number x, find a pair (a,b) in A such that a+b = x

solution:
a+b = x
b = x-a    
known elements in the above eq. are: x and array A

lets say the array A contains = (1,20,5,6,9,2,10) and x= 8; we need to find (a,b)
1. traverse through array:
   0 to n-1:
       a = 1 then find b i.e., b = x-a = 8-1 = 7
       a = 20 then find b; b = -12
       a = 5 then find b; b= 3
       a = 6 then find b; b=2
       a = 9 then find b; b= -1
       a= 2 then find b; b=6
       a=10 then find b; b=-2

#challenges here: 1. Does the array contain duplicates; 2. Does the array contain negative values
'''
import numpy as np

def find_b_with_duplicate_tuples(A,x,dic_A):
    for a in A:
        if(x-a in dic_A):
            dic_A[x-a] -= 1
            yield (a, x-a)
        else:
            continue

def find_b_unique_tuples(A,x,dic_A):
    for a in A:
        dic_A[a] -= 1
        if(x-a in dic_A and dic_A[x-a] > 0):
            dic_A[x-a] -= 1
            yield (a, x-a)
        else:
            continue

#Given array A
A = np.array(list(map(int,input("A?  ").split())))
dic_A = dict()
x = int(input("x?  "))
#Iterate through the input and create a dictionary
for i in A:
    if i in dic_A:
        dic_A[i] += 1
    else:
        dic_A[i] = 1

print("Unique tuples whose sum is {}".format(x))
for a,b in (find_b_unique_tuples(A,x,dic_A)):
    print(a,b)

print("Tuples including duplicates whose sum is {}".format(x))
for a,b in (find_b_with_duplicate_tuples(A,x,dic_A)):
    print(a,b)    
