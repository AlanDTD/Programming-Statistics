# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:34:03 2021

@author: aland
"""
import random as rd



guess_number = 0
player_distance = []
mean1 = []
mean2 = []
player = 1
SD1= []
SD2 = []
rounds = 0
player1_wins = 0
player_guess_count = 1



def mean(lst):
    return sum(lst) / len(lst)

def std(lst):
    SD = 0
    for i in range(len(lst)): 
        SD = SD + (lst[i] - mean(lst))**2
    return (SD/(len(lst) - 1))**0.5

def mean_comp(mean1,mean2,sd1,sd2):
    return


def win(Attempts, #win conditions 

rounds = 0


print("Let's play a guessing game \n")
print("Rule: each player takes a turn to pick a number, the person who gets the right number within 3 guesses wins \n")


rounds = int(input("How many rounds would you like to play "))*2
print('\n')

    
for i in range(rounds):
    guess_number = rd.randint(1,10)
    print("Player %d" %player)
    
    while True: #Guess Loop
        player_guess = int(input("Please guess a number between 1 to 10: "))
        if player_guess < guess_number:
            print("Your number is too low")
        elif player_guess > guess_number:
            print("Your number is too high")
        elif player_guess == guess_number:
            print("Congratulations you got the right number")

    
    if player_guess_count > 3:
        if player == 1: 
            mean1.append(mean(player_distance))
            SD1.append(std(player_distance))
        else:
            mean2.append(mean(player_distance))
            SD2.append(std(player_distance))
    
    print(player, " wins this round")
    if i % 2 == 0: #change player and resets counter
        player = 2 
    else: 
        player = 1
    
    player_distance = []
    player_guess = 0
    i = i + 1
    
print(mean1,SD1)
print(mean2,SD2)
    
    
    
    
    
    





