# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:58:25 2021

@author: aland
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:34:03 2021

@author: aland
"""
import random as rd

player_lst = {"Player 1": [], "Player 2": []}
count1 = 0
count2 =0
score_d = {"Player 1": 0, "Player 2": 0, "Tie":1 }
game_count = 0

def mean(lst):
    return sum(lst) / len(lst)
  

def std(lst):
    SD = 0
    for i in range(len(lst)): 
        SD = SD + (lst[i] - mean(lst))**2
    return (SD/(len(lst) - 1))**0.5

def mean_comp(lst1, lst2):
    mean1 = mean(lst1)
    mean2 = mean(lst2)
    SD1 = std(lst1)
    SD2 = std(lst2)
    return (mean1-mean2)/((SD1/game_count)+(SD2/game_count))**.5


def score(guess1,guess2, List1, List2): #Function to determine winning outcome 
    if guess1 <=3 and guess2 <=3:
        score_d["Tie"] +=1
        return "Tie"
    elif guess1 <=3:
        score_d["Player 1"] += 1
        return "Player 1 wins"
    elif guess2 <=3: 
        score_d["Player 2"] += 1
        return "Player 2 wins"
    else:
        if mean_comp(player_lst["Player 1"],player_lst["Player 2"]) < -1.95:
            score_d["Player 1"] += 1
            return "Player 1 is better at guessing"
        elif mean_comp(player_lst["Player 1"],player_lst["Player 2"]) > 1.95:
            score_d["Player 2"] += 1
            return "Player 2 is better at guessing"
        else:
            score_d["Tie"] +=1
            return "Both players are statistically even"

    
        


#Guess Game
while True:
    
    guess_num = rd.randint(1,10)
    guess_num2 = rd.randint(1,10)
    
    game_state = input("Please please enter to play or N to exit")
    game_count += 1
    
    if game_state == "N":
        print(score_d)
        break
    
    while True:
        count1 += 1
        player_num = int(input("Player 1 Guess a number: "))
        player_lst["Player 1"].append(abs(guess_num - player_num))
    
        
        if guess_num == player_num:
            print("You have guess correctly")
            break


    print("player two turn")
    while True:
        count2 += 1
        player_num = int(input("Player 2 Guess a number: "))
        player_lst["Player 2"].append(abs(guess_num2 - player_num))
    
    
        if guess_num2 == player_num:
            print("You have guess correctly")
            break 

    print(score(count1,count2,player_lst["Player 1"],player_lst["Player 2"]))
    count1 = 0
    count2 = 0
    