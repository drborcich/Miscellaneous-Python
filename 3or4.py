#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:00:58 2019

@author: drb
"""

import random as rand


# Creates random array of numbers, and will shift 
# numbers such that every 3 is followed by a 4, and 
# the 3's stay in place, and no numbers are added
# ( idea taken from CodingBat)


# create random nums array
def get_nums():
    length = rand.randint(1,10)
    nums = []
    for i in range(length):
        nums.append(rand.randint(1,4))
    return(nums)
    
    
def main():
    nums = get_nums()
    new_arr = []  
    j = 0
    three_tot = 0    # count total 3s in nums
    for i in nums:
        if nums[i] == 3:  # ensure presence of 4s in array
            three_tot += 1
            nums.append(4)
    placed = 0        # count placed 3s in new_arr
    while (j < len(nums)):
        #print("j= " + str(j))
        #print("k= " + str(k))
        if (nums[j] == 3):
            new_arr.append(3)
            new_arr.append(4)
            placed += 1
            
        elif (nums[j] != 4 ):
            new_arr.append(nums[j])
        elif (nums[j] == 4 and placed == three_tot):
            new_arr.append(nums[j])
        j += 1


    print("nums: " + str(nums))
    print("new: " + str(new_arr))
        
    return 

    
    
main()
