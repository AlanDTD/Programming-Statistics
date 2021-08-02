#Black Jack 

import random as rd #random module


print("Hi There welcome to a game of 21 ")


player_value = 0

new_card = 0

player_state = input("To press enter to draw a card to start \n").upper()

while player_state != 'S' and player_value <= 21:
    
   
    #Prompt	the	player to draw one card and display the value of the card drawn.	
    new_card = rd.randint(2,11)
    if player_value + new_card > 21 and new_card == 11:
        player_value += 10
    player_value = player_value + new_card
    
    print("You have drawn a %d," %new_card)
    
    #Ask whether they want to draw another card, or finish their game.
    print("You currently have a total of %d! \n" %player_value)
    if player_value <= 21: #This to hide the input if the value has exceed 21 as we don't require the input
        player_state = input("To press enter to draw a card or enter S to stay \n").upper()

    

else: 
    if player_value == 21:
        print("You Win!")
    elif player_value > 21:
        print("You Bust! better luck next time")
    else:
        new_card = rd.randint(2,11)
        if player_value + new_card > 21:
            print("good timing as you would have busted! with", player_value + new_card)
        else: 
            print("You could have kept going as you were under 21 with", player_value + new_card)
        
