#Black Jack 

import random as rd #random module
import sys #used to cancel game




    #option to exit with  N
print("Please enter Y to draw a card E to exit: ")

player_input = input()
player_value = 0
new_card = 0
    
    

while True: #main game loop

    if player_input == 'E':
        print('Thanks for playing')
        sys.exit()

    #Card Draw 
    if player_input == "Y":
        new_card = rd.randint(2,11) #New Card drawn value
        print("You have drawn %d \n" %new_card)
        player_value = player_value + new_card #Add to card value
        
        #Check for winning conditions, and resets variables
        if player_value == 21:
            print("21! You win!")
            player_value = 0 
        #Check if last card is ace whether it will cause a burst or not
        if new_card == 11 and player_value > 21:
            player_value = player_value - 10 #Very hacky way of making the value 1
        
        #losing condition, plus resetting variables back to 0
        elif player_value > 21:
            print("Bust! you have %d please try again \n" %player_value)
            player_value = 0 
    
    #Checks the game state, if player has restarted or still playing
    if player_value == 0:
        print("Please enter Y to draw a card or E to exit")
        player_input = input()
    else:
        print("You currently have %s enter Y to draw another card, E to exit" %player_value)
        player_input = input()





    
    



    