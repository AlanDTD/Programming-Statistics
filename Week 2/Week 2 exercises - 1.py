# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:50:05 2021

@author: alandtd3
"""

#Exercises A

for i in range(1,11):
    print(i)
    


#Exercises B

import random as rd #Import Random 

temp_num = rd.randint(16,35) #Generate a random number between 16 - 35

print('Temperature Number', temp_num)

while 20 <= temp_num <= 30:
    print("The Weather is Fine!")
    break


    
    




    
days_of_week = ['Monday','Tueday','Wednesday','Thursday','Friday','Saturday','Sunday']

for i in days_of_week:
    print(i)
    

i = 0

while i < len(days_of_week):
    print("Today is", days_of_week[i])
    i += 1
    