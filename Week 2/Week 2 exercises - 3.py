# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:53:17 2021

@author: aland
"""

nums = eval(input("Enter at least 5 numbers separated by commas!"))

sum_num = 0
count_int = 0
count = 0


if type(nums) == tuple: #Checks if ithe value is a tuple
    while len(nums) < 5: #Checks the tuples lengeth is at least 5
        print("You do not have enough number")
        nums = eval(input("Please try again, at least 5")) #reruns the loop until the right number
    else:
        for i in range(len(nums)): #iterates and sums the numbers
            if type(nums[i]) == int:
                sum_num = sum_num + nums[i]
                count_int = count_int + 1
        mean_value = float(sum_num) / count_int
        print("The list was %s with a mean of %5.2f, there was %d valid numbers" %(nums, mean_value, count_int))
else:
    print("This is not a tuple") 
    nums = eval(input("Please use commas to seprate")) 
    