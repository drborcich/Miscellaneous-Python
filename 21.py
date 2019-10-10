#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:45:10 2019

@author: drb
"""
import random as rand

RANK = 0
REMAINING = 1

print("No splits yet, one deck in play...\n")

####     IMPLEMENTATION     ####

class Hand:
    def __init__(self, owner):
       self.owner = str(owner)
       self.score = 0    # int representing sum/score of cards
       self.hand = ""    # string of chars representing cards in hand
       self.drawn = 0    # count if deck is empty  
       self.lost = False # for busted, or score comp
       self.blackjack = False  # is it a blackjack 21
       self.stay = False         
       self.aceLow = False
       #self.lenHand = 0
       
    def deal_to(self, deck):
           # pick from card groups (rank_index) 2 thru 14
        found_card = False
        while found_card == False:
            rank_index = rand.randint(0,12)
            rank = deck[rank_index][RANK]
            remaining = deck[rank_index][REMAINING]
            #print self.aceLow, self.owner
            
            # if there are cards of that rank remaining...
            if remaining > 0 :
                found_card = True
                self.update_score(rank)
                if self.drawn == 0:
                    self.hand += (str(rank)) 
                else:
                    self.hand += (" " + str(rank)) 
                if self.score > 21 and self.aceLow == False:
                    if "A" in self.hand:
                        self.score -= 10
                        self.aceLow = True
                    
                # decrement number of remaining
                remaining -= 1
                self.drawn += 1    # to check if deck is empty @ 52
                return(deck)
        return
        #card_and_deck = [card, deck]
        #return card_and_deck
    
    def print_hand(self):
        print self.owner + ": [" + self.hand + "] " + str(self.score) + "\n"
        if self.score > 21:
            print "Busted! \n"
        return
        
    def update_score(self, rank):
        if type(rank) == str:
            if rank ==  "A":
                self.score += 11
            else:
                self.score += 10
                if "A" in self.hand and len(self.hand) == 2:
                    self.blackjack = True                
        else:
            self.score += rank 
        return
    
    def score_check(self, end):
        if self.score == 21:
            self.stay = True
            # Aces low handled in Hand.deal_to
        if self.score > 21:
            self.lost = True
            self.stay = True
                     
        # dealer stay on 17  *** SOFT 17
        if self.owner == "Dealer" and self.score > 17:
            self.stay = True
        return end

#####   CLIENT  ##### 
              
 # deck:  0 to 14, 2D array -- "list" in Python
 # index [RANK,REMAINING]
def fresh_deck():
    deck = []
    i = 0
    while i < 9:
        deck.append([i+2,4])
        i += 1
    while i < 13:
        if i == 9:
            deck.append(["J", 4])
        if i == 10:
            deck.append(["Q", 4])
        if i == 11:
            deck.append(["K", 4])
        if i == 12:
            deck.append(["A", 4])    
        i += 1           
    return deck

# takes player chips, confirms bet 
def get_bet(player_chips):
    bet = input("Place your bet >> ")
    if bet > player_chips:
        print "\n Don't be greedy \n"
        get_bet(player_chips)
    if bet <= 0:
        print"\n No cheating! \n"
        get_bet(player_chips)
    return bet

# gets player hit/stay command
def hit(hand,deck):
    while hand.stay == False:
        if hand.owner == "Player":
            hit = input("Hit? (0 = Y, 1 = N)")
        if hit == True:
            hand.deal_to(deck)
    return

# hand server 
def play_hand(player_chips, deck):
    print("  Dealing...  \n")
    end = False
    dealer = Hand("Dealer")   # use the class...
    player = Hand("Player")
    if player.drawn + dealer.drawn == 52:
        print "Fresh deck \n"
        deck = fresh_deck()
    print("Chip stack: " + str(player_chips))
    bet = get_bet(player_chips)

    # start the hand - display only 1 of dealer's cards
    dealer.deal_to(deck)
    dealer.print_hand()
    dealer.deal_to(deck)
    player.deal_to(deck)
    player.deal_to(deck)
    player.print_hand()
    end = player.score_check(end)
    end = dealer.score_check(end)
    if player.score == 21:
        print "Blackjack! \n"
        dealer.print_hand()
        if dealer.score != 21:
            print "You win \n"
            return(round(player_chips*2.5))             
          
    while player.stay == False and end == False:
        hit = input("Hit? (0 = Y, 1 = N) << ")
        if hit == 0:
            player.deal_to(deck)
            end = player.score_check(end)
            player.print_hand()
        else:
            player.stay = True
            
    dealer.print_hand()
    while dealer.stay == False and end == False:
        dealer.deal_to(deck)
        end = dealer.score_check(end)
        dealer.print_hand()
    
    # to get to this point, end must be true...

    if dealer.lost == True and player.lost == False:
        if player.blackjack == True:
            player_chips += bet*.5
        player_chips += bet
        print "Hand won \n"
    if player.lost == True and dealer.lost == False:
        player_chips -= bet
        print "Hand lost \n"
    #if player.lost and dealer.lost:
    #    print "Push \n"
    elif player.lost == False and dealer.lost == False:
        if player.score > dealer.score:
            if player.blackjack == True:
                player_chips += bet*.5
            player_chips += bet
            print "Hand won \n"
        if dealer.score > player.score:
            player_chips -= bet
            print "Hand lost \n"

    return (player_chips)


def main():
    player_chips = 100
    while player_chips > 0: # and play_again == y:
        deck = fresh_deck()
        player_chips = play_hand(player_chips, deck)
        if player_chips == 0:
            print("\n You're broke! ")
            
            #play_again = (input("Play again? (y/n) >> " ))
            #play_again = str(play_again)
    
    return()
    
main()
    