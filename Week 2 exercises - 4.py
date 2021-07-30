# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 21:21:49 2021

@author: aland
"""


nums = eval(input("Enter at least 3 numbers separated by commas!"))

sum_num = 0
count_int = int(0)
count = 0
SD = float(0)


if type(nums) == tuple: #Checks if ithe value is a tuple
    while len(nums) < 3: #Checks the tuples lengeth is at least 3
        print("You do not have enough number")
        nums = eval(input("Please try again, at least 3")) #reruns the loop until the right number
    else:
        for i in range(len(nums)): #iterates and sums the numbers
            if type(nums[i]) == int:
                sum_num = sum_num + nums[i]
                count_int = count_int + 1
        mean_value = int(sum_num / count_int) # obtain mean
        
        # Calculates the St.dev
        for i in range(len(nums)): 
            if type(nums[i]) == int:
                SD = SD + (nums[i] - mean_value)**2
        sdev = (SD/(count_int - 1))**0.5
        
        print("The standard deviation for the list of %s is %5.2f" %(nums,sdev))

    