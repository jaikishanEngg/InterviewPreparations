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
import math
def isElementAtCurrentIndexOne(inputArray, index):
    return inputArray[index] == 1

def isElementAtCurrentIndexZero(inputArray, index):
    return inputArray[index] == 0

def getMiddleIndex(lowerIndex, higherIndex):
    return ceil((lowerIndex + higherIndex)/2)

def getPreviousTwoExponentIndex(index):
    return 
    
def linearlySearchForElementOne(inputArray, startIndex, endIndex):
    try:
        for index in range(startIndex, endIndex):
            if(isElementAtCurrentIndexOne(inputArray,index)):
                return index
    except IndexError:
        return -1
        #print("Element 1 does not found in the input array!")
        
def sliceArrayAtFirstIndexOfElementOne(inputArray):
    '''
    In the unknown size of the binary array, where all the 0's at the left and all the 1's at the end
    As we need to find the first index of 1, as the size is unknown we cannot apply binary search.
    So, we will try to exponentially(2^) increase the step to search for 1 in this function
    While increasing the index step exponentially, it may go beyond the actual size. 
    so handling indexError exception and taking the sub-array by the previous step index and searching linearly
    if exception doesn't raise, then we take the proper sub-array and apply binary search on it to find the first index of 1 in that sub-array
    '''
    try:
        curr_iteration = index =  1
        errorFlag = False
        while(True):
            if(isElementAtCurrentIndexOne(inputArray,index)):
                #return the upper index with errorstatus False
                return index, errorFlag
            else:
                index = int(math.pow(2,curr_iteration))
            curr_iteration += 1
    except IndexError:
        errorFlag = True
        #return the upper index with errorstatus True
        return index, errorFlag   

def searchForElementOneApplyingBinarySearch(inputArray,lowerIndex,higherIndex, searchElement = 1):
    '''
    As the all zeros are left and all the ones are at the right - the array is already sorted.
    So binary serach can be applied.
    '''
    middleIndex = getMiddleIndex(lowerIndex,higherIndex)
    if(inputArray[middleIndex] == searchElement and inputArray[middleIndex - 1] != searchElement):
        return middleIndex
    elif(inputArray[middleIndex] < searchElement):
        lowerIndex = middleIndex
        return searchForElementOneApplyingBinarySearch(inputArray,lowerIndex,higherIndex)
    else:
        higherIndex = middleIndex
        return searchForElementOneApplyingBinarySearch(inputArray,lowerIndex,higherIndex)
    
def findStartingIndexOfElementOne(inputArray):
    higherIndex, errorFlag = sliceArrayAtFirstIndexOfElementOne(inputArray)
    lowerIndex = floor(higherIndex/2)
    #floor(2** (int(log(higherIndex,2)) - 1))
    if(errorFlag):
        #As the step index raised the error, from the previous step index perform linear search
        return linearlySearchForElementOne(inputArray, lowerIndex, higherIndex)
    else:
        #As there is no index error, we have got a fixed proper sub-array; so we know the boundaries and can apply binary search
        return searchForElementOneApplyingBinarySearch(inputArray,lowerIndex,higherIndex)
    
#z = list(map(int,"0 0 0 0 0 0 1 1 1 1 1 1 1 1 1".split()))
rawinputArray = input().split()
inputArray = list(map(int,rawinputArray))

print(findStartingIndexOfElementOne(inputArray))
