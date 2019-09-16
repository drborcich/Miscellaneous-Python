#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 17:15:37 2019

@author: drb
"""

import matplotlib.pyplot as plt
#import numpy as np


# retirement calculator - takes current saved net worth,
# increments over years using exponential growth plus
# growth in savings contributions -- assumes no taxes
# on growth (like in a 401(k) or other retirement account)
# also assumes 7% growth rate, reflecting historically 
# reasonable rates over the LONG TERM 
def main():
    nw = float(input("Current savings: "))
    contribution = float(input("Contribution: "))
    contribution_growth = float(input("Contribution growth %: "))
    contribution_growth = contribution_growth/100
    time = 0
    exp_return = .07
    horizon = input("Time horizon (yrs): ")
    nw_arr = []
    time_arr = []
    contrib_arr = []
    for time in range(horizon):
        contribution = contribution*(1+contribution_growth)
        nw = nw + nw*exp_return + contribution
        contrib_arr.append(contribution)
        nw_arr.append( nw)
        time_arr.append( time)

    plt.plot(time_arr, nw_arr, 'go')
    plt.plot(time_arr, contrib_arr, 'bs')
    plt.axis([0, horizon, 0, (nw)])
    plt.show()
    print "Horizon year contribution: " + str(round(contribution, 2))
    print "NW at time horizon: " + str(round(nw, 2))
    
    
    
    
    
    return
    
    
    
    
    
    
    
main()