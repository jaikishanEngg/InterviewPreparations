# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:29:33 2020

@author: Kishan
"""

'''
problem statement: Given an array A of size n, find the element that occurs more than n/2 times
solution:
    Moore voting algorithm:
    1. Each element in the array votes(counts) for itself
    2. When the other element appears in the lookup it can use the upvotes from the majority element(to devote) 
        or if upvotes is already 0 then it can count to 1 and being the majority element
    3. The majority voter will have atleast 1 vote at the end of the traversal
    4. At the end, we need to cross check the no.of times the voter has appeared in the list
    
time coplexity:
    1. To give up and down votes for each element we have to scan the entire array once, so it is O(n)
    2. At the end, we need to cross verify whether the voter is the answer - so we need to ensure the count is majority for that element. So it is O(n)
    3. Therefore, it is O(n)+O(n) = O(n)
    
'''
from math import floor
def majority_element(a):
    '''
    return an expcted majority element by applying moore voting algo.,
    '''
    votes = 0
    voter = None
    for v in a:
        if votes == 0:
            #First element/voter or when all the upvotes are devoted by other and equalised to 0
            voter = v
            votes = 1
        else:
            #from second element or from the unequalized condition
            if(v == voter):
                #upvote(increase) the vote count of the voter - self upvote
                votes += 1
            else:
                if(votes > 0):
                    #devote 
                    votes -= 1
                else:
                    #when the majority elements are devoted by other elements; when votes == 0, a new voter with upvote 1 will lead
                    voter = v
                    votes = 1
    return voter

def verify_majority_element(a, eme):
    '''
    return a boolean value by verifying the expected majority element
    '''
    return a.count(eme) > floor(len(a)/2)

#input array
a = list(map(int,input("Array?   ").split()))   
eme = majority_element(a)
if(verify_majority_element(a, eme)):
    print("Majority element in the array {} is : {}".format(a,eme))
else:
    print("No majority element in the array {}".format(a))