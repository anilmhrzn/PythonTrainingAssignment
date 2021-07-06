# Ask enter to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a combination of these two newly generated random numbers.

# formula for combination is c = n!/r!(n-r)!


import math        
import random      


# taking input from user
start= int(input("Enter the starting number"))
end= int(input("Enter the ending number"))

# generating random number

number1= random.randint(start,end)
number2 = random.randint(start,end)

# factorizing the number
num1fac= math.factorial(number1)       # n!
num2fac= math.factorial(number2)       # r!

# testing
print(number1)
print(number2)

# swaping the value if the num1 is smaller then num2
if number1<number2:
    number1,number2=number2,number1

# (n-r)
subnumber=number1-number2

# factorizing the subnum -- (n-r)!
subnumber2fac = math.factorial(subnumber)

# combination formula
combination=int(num1fac/(num2fac*(subnumber2fac)))

# output
print(combination)