# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:22:07 2020

@author: Kishan
"""

'''
Problem statement:
    Find the number that is occuring odd number of times in a given array of size n

Approach
1. Naive approach is to start with the each element and count how many time it has occured in the array
So, for each element we have to compare/run through (n-1) times to get the count
Therefore it is (n)^2 time complexity and O(1) space complexity
2. We can use hash table and for the new element the count is 1, for the existing element we will add 1 more
O(n) time complexity and for hash table O(n) space complexity
3. XOR (Exclusive OR), which is also called modulo2 sum (means add two numbers and %2)
O(n) time complexity and O(1) space complexity
'''

#Assuming that there exists only one num that occurs odd number of times in the array
input_list_of_nums = list(map(int,input().split()))

def find_odd_occuring_num(inp):
    xor = inp[0]
    for i in range(0,len(inp)):
        xor ^= inp[i]
    return xor

print(find_odd_occuring_num(input_list_of_nums))
    
        
