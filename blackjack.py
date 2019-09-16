#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:55:02 2019

@author: drb
"""

import random as rand

# Black Jack Simulator !


class Hand:
   def __init__(self, owner, score, hand):
       self.owner = ""
       self.score = 0
       self.hand = ""
       
 # deck:  0 to 14,  dict from 0 to 14    
def fresh_deck():
    deck = [[]]
    for i in range(15):
        if i == 11:
            deck[i] = ["J",4]
        if i == 12:
            deck[i] = ["Q",4]
        if i == 13:
            deck[i] = ["K",4]
        if i == 14:
            deck[i] = ["A",4]
# dont actually need 0 or 1 index bc no correpsonding card, can ignore
        else:
            deck[i] = [i,4]
        
        
    return deck

# game server
def play_hand(player_chips):
    deck = fresh_deck()
    print("Dealing...")
    dealer_score = 0
    dealer_hand = ""
    player_score = 0
    player_hand = ""
    while end ==  False:
        end = True
        
    
    
    return player_chips
    

def main():
    player_chips = 100
    while player_chips > 0:
        player_chips = play_hand(player_chips)
    
    print("Game over, you're broke! ")
    again = input("Play again? ")
    if again == True:
        main()
    
    return()
    
main()
    
    
    
    
    