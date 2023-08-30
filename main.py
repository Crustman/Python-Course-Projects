


# print("You are targeting " + input("What ip: "))

#This varable
# 
# print("This is my Program!!")
# petn = input("What is your pets name?: ")
# cityb = input("What city where you born in? ")

# print(f"\nSo your cybername is @cyber{petn} and your from {cityb}!!")

# fnum = input("What is the first number ")
# snum = input("What is the second number ")

# if fnum > snum:
#     print("The first number is bigger😮")

# elif fnum == snum:
#     print("the two numbers are equal!!😊😊😊")    

# else:
#     print("The second number is larger😁")
    

#num = input("Please, enter in your number ")

# gradea = (90, 100)
# gradeb = (80, 89)
# gradec = (70, 79)
# graded = (60, 69)
# gradef = (50, 59)

# score = input("Enter your score: ")
# score = (int(score))

# if score >= 90:
#     print("You get a Grade of A")
# elif score >= 80:
#     print("You get a Grade of B")
# elif score >= 70:
#     print("You get a Grade of C")
# elif score >= 60:
#     print("You get a Grade of D") 
    
# else:
#     print(" You should study more!!")
    
    
# num = int(num)

# if num >= 90:
#     age = int(input(" What is your age? "))
#     if age < 10:
#         print("Your grade is an A+")
#     else:
#         print("Your grade is a A")
            
# elif num >= 80:
#     if age < 10:
#         print("Your grade is an A+")
#     else:
#         print("Your grade is a A")
  
# elif num >= 70:
#     print(" You recieve Grade C")
    
# elif num >= 60:
#     print(" You recieve Grade D")
    
# else:
#     print(" You recieve Grade F")


# for Loops

# fruits = ["apple", "banna", "cherry"]

# for i in fruits:
#     print(i + " pie")

# total = 0

# number = int(input('Enter a number: '))

# # add numbers until number is zero
# while number != 0:
#     total += number    
    
    
#     number = int(input('Enter a number: '))
    

# print('total =', total)

# for range loop

# for num in range(0, 100, 2):
#     if num % 3 == 0:
#         print(num)

# fizzbuzz
# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz

# for num in range(1, 100):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#     elif num % 3 ==0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")    
    
#     else:
#         print(num)
# for loops
#names = ["Dave", "Sara", "John"]

# for x in names:
#     print(x)
# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# 
# for x in range(4):
#     print(x)     

# for x in range(5):
#     print(x)     
# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Glad thats over!!")     

 
 
 
        
# # program to calculate the sum of numbers
# until the user enters zero

# total = 0

# number = int(input('Enter a number: '))

# # add numbers until number is zero
# while number != 0:
#     total += number    # total = total + number
    
#     # take integer input again
#     number = int(input('Enter a number: '))
    

# print('total =', total)          

# age = 32

# # the test condition is always True
# while age > 18:
#     print('You can vote')  

# fruits = ["apple", "banna", "cherry"] 

# for i in fruits:
#     print(i + " pie")    
    



import time
choice = int(input("What number would you like to choose? "))

def function(choice):
    for num in range(choice):
        if num % 3 ==0 and num % 5 ==0:
            print("fizzbuzz")
        elif num % 3 == 0:
              print("fizz")
        elif num % 5 == 0:
              print("buzz")
        else:
            print(num)

print("about to run the program")   
time.sleep(5)   
function(choice)