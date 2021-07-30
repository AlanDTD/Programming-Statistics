# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:25:38 2021

@author: aland
"""

    #Check if player wants to draw again
    print("Enter Y to draw another card, S to stay or N to exit")
    player_input = input()
    if player_input == "Y
        new_card = rd.randint(2,11)
        print("You currently have %s and you drew a %s", %(player_card, new_card))
        player_card = player_card + new_card
        print("You are now on $s", %player_card)
        