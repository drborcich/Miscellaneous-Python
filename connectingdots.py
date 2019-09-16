#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:17:00 2019

@author: drb
"""
 
import random as rand


def make_page():
    letters = ["a", "b", "c", "d", "e"]
    page = ""
    i = 0
    placed = 0
    near_end = 104
    # fill page 
    while i < 110:
        rem_letters = len(letters)
        #print(str(max_letters))
        if (i % 11 == 0):
            page =  page  + "\n"
        # add rand letter, then remove from pool
        elif rem_letters > 0 and rand.randint(0,15) == 1:
            selection = rand.choice(letters)
            page = page + selection
            letters.remove(selection)
            placed = placed + 1
        # add remaining letters if incomplete, then remove
        elif rem_letters > 0 and i > near_end:
            last_few = letters[0]
            page = page + last_few
            letters.remove(last_few)
        # blank space   
        else: 
            page = page + "_"
        i = i + 1
    #print(placed)
    #print(letters)
    #print(rem_letters)
    return(page)

def main():
 
    print(make_page())
    return  0








main()
