#Black Jack 

import random as rd #random module


print("Hi There welcome to a game of 21 ")

while True: #Start game loop
    
    #game code    

    player_value = 0
    new_card = 0
    
    player_state = input("To press enter to draw a card to start \n").upper() #first card draw

    while player_state != 'S' and player_value < 21:
    
        new_card = rd.randint(2,11)  #Random card draw
        
        if player_value + new_card > 21 and new_card == 11: # check if ace was drawn and if it causes a bust if it does makes the card value 1
            new_card = 1 
        player_value = player_value + new_card
        
        print("You have drawn a %d," %new_card)
        print("You currently have a total of %d! \n" %player_value)
        if player_value < 21: #This to hide the option for players to draw another card as score conditions are met
            player_state = input("To press enter to draw a card or enter S to stay \n").upper() #Ask whether they want to draw another card, or stay
            
            
    else:  #score conditions 21 or bust
        if player_value == 21:
            print("You Win!")
        elif player_value > 21:
                print("You Bust! better luck next time")
        else: #Next card drawn if player decided to stay
            new_card = rd.randint(2,11)    
            if player_value + new_card > 21 and new_card == 11: #changes ace value depending if greater or less than 21
                new_card = 1
            elif player_value + new_card > 21: 
                print("good timing as you would have busted! with", player_value + new_card) 
            elif player_value == 21:
                print("Too bad you could have gotten 21!")
            else: 
                print("You could have kept going as you were under 21 with", player_value + new_card)
        if input("\nWould you like to play again? press enter to play again or enter 'N' to exit game \n>>> ").upper() == "N": #End game loop
            print("Thanks for playing")
            break
