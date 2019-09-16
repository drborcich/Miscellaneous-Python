#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:44:24 2019

@author: drb
"""


# Calculates the angle between the hour and minute
# hands on a typical analog clock

# (idea taken from Fullstack Coding Assessment

def clock(hour, minutes):
    hour_deg = hour*30 + (minutes/60)*30
    min_deg = minutes*6
    #print(hour_deg)
    #print(min_deg)
    angle = abs(min_deg - hour_deg)
    if (angle > 180):
        angle = 360 - angle
    return angle
    

def main():
    hour = input("Enter hours: ")
    minutes = input("Enter minutes: ")
    
    hour = float(hour)
    minutes = float(minutes)
    angle = (clock(hour,minutes))
    print("angle = " + str(angle))
    return()
    
main()
    
    
    
    
    
    
    
    
    
    
    