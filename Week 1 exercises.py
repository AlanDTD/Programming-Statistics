'Week 1'
'Exercise 1'
print('Hello World Alan')

'------------------------'

'Exercise 2'
x = 5
y = 1
z = 5

res1  = x < y
print(res1)

res2 = y < x and z < y
print(res2)

res3 = x == z
print(res3)

res4 = y < x or y == z
print(res4)

'------------------------'

'Exercise 3'

def exc1(a,b):
    return a < b or a + b < 10

print("Table 1")
print(exc1(1,1)) #True
print(exc1(5,5)) #False
print(exc1(4,3)) #True
print(exc1(7,9)) #True
print(exc1(3,4)) #True

def exc2(a,b):
    return not (a < b or a + b < 10)

print("table 2")
print(exc2(1,1)) #True
print(exc2(5,5)) #True
print(exc2(4,3)) #True
print(exc2(7,9)) #False
print(exc2(3,4)) #True

def exc3(a,b):
    return a < b and a + b < 10

print("Table 3")
print(exc3(1,1)) #False
print(exc3(5,5)) #False
print(exc3(4,3)) #False
print(exc3(7,9)) #False
print(exc3(3,4)) #True

def exc4(a,b):
    return not(a < b and a + b < 10)

print("Table 4")
print(exc4(1,1)) #True
print(exc4(5,5)) #True
print(exc4(4,3)) #True
print(exc4(7,9)) #True
print(exc4(3,4)) #False

'------------------------'

'Exercise 4'

print('exercise 4a')

count = 21

print(0 <= count <= 20)



print('exercise 4b')

count = 21

print(count >= 20)

print('exercise 4c') 

s1 = 4
s2 = 4
s3 = 4

print((s1 > 0 and s2> 0 and s3 > 0) and (s1 + s2 > s3 or s2 + s3 > s1 or s1 + s3 > s2)) 

print('exercise 4d') 

print((s1 > 0 and s2> 0 and s3 > 0) and (s1 + s2 > s3 or s2 + s3 > s1 or s1 + s3 > s2) and (s1 == s2 == s3))

print('exercise 4e')

print((s1 > 0 and s2> 0 and s3 > 0) and (s1 + s2 > s3 or s2 + s3 > s1 or s1 + s3 > s2) and (s1 == s2 or s2 == s3 or s1 == s3))

print('exercise 4f')

print((s1 > 0 and s2> 0 and s3 > 0) and (s1 + s2 > s3 or s2 + s3 > s1 or s1 + s3 > s2) and not(s1 == s2 and s2 == s3 and s1 == s3))

print('exercise 4f optional')
print((s1 > 0 and s2> 0 and s3 > 0) and (s1 + s2 > s3 or s2 + s3 > s1 or s1 + s3 > s2) and not(s1 == s2 == s3))

'------------------------'

print('exercise 5a')
a= 2
b = 3
if a < b :
    print('a is larger than b')
else:
    print('b is larger than a')    
    a = +1
    b = -a
 
print('a=', a, 'b=', b)


'------------------------'

print('exercise 5b')

if a + b > 3 :
    if b < 5 :
        print(b)
    elif a > 2:
        print(a)
    else:
        print(a + b)
else:
    print(a - b)
print(a, b)

'------------------------'

print('exercise 6a')

import random

randomnumber = random.randint(1,10)
print(randomnumber)

print('exercise 6b')

#print("please input number: ")

#player_input = int(input())
#randomnumber = random.randint(1,10)
#if player_input == randomnumber:
#    print("well done you guessed right")
#else:
    #print("Nope try again the correct number is" , randomnumber)

print('exercise 7')


#print("please input number: ")

#player_input = int(input())
#randomnumber = random.randint(1,10)

#print("You guessed:", player_input)
#print("The random number is", randomnumber)

#if player_input == randomnumber:
    #print("Well done you guessed it")
#else:
 #   print("Too bad - better luck next time!")

print('exercise 8')

#print("please input number: ")
#player_input = int(input())
#randomnumber = random.randint(1,10)


#print("You guessed:", player_input)
#print("The random number is", randomnumber)


#if player_input == randomnumber:
#    print("Well done you guessed it")
#elif player_input > randomnumber:
#    print("Too high!")    
#    print("Too bad - better luck next time")
#elif player_input < randomnumber:
#    print("Too low!")
#    print("Too bad - better luck next time")

#print('exercise 9a')
#print("Please input first number")
#input_1 = int(input())
#print("Please input second number")
#input_2 = int(input())
#if input_1 > input_2:
#    print(input_1, "is larger")
#print(input_2, "is larger")


print('exercise 9b')    

#print("please input your name")
#name = input()

#if name == "Alan":
#    print("Same as me!")
#else:
#    print("Not the same as my name!")

print('exercie 10 two up')

#0 for heads 1 for tails

coin1 = random.randint(0,1)
coin2 = random.randint(0,1)

if coin1 == 0:
    print("Coin 1 = Head")
else:
    print("Coin 1 = Tail")

if coin2 == 0:
    print("Coin 2 = Head")
else:
    print("Coin 2 = Tail")

if coin1 == 0 and coin2 == 0:
    print("Spinner Wins! Two heads!")
elif coin1 == 1 and coin2 == 1:
    print("Spinner Losses! Two Tails!")
else:
    print("Throw again")
    
print("Thanks for playing")