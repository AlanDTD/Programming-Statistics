# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:05:57 2021

@author: aland
"""

#Loops and input Processing

nums = tuple(input("Enter at least 5 numbers separated by commas!"))
print(len(nums))
print(nums)

sum_num = 0
count = 0



if type(nums) == tuple: #Checks if ithe value is a tuple
    while len(nums) < 5: #Checks the tuples lengeth is at least 5
        print("You do not have enough number")
        nums = tuple(input("Please try again, at least 5")) #reruns the loop until the right number
    else:
        for i in range(len(nums)): #iterates and sums the numbers
            if type(nums[i]) == int:
                sum_num = sum_num + nums[i]
            else:
                count = count + 1
    
        print("The total sum of the numbers are %d with and %d NaN" %(sum_num, count))
else:
    print("This is not a tuple") 
    nums = tuple(input("Please use commas to seprate"))
    