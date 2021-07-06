# Write a Python code that inputs input from the user and calculate its square root.
import math 
number=int(input("Enter a number to find its square root:"))
result=float(math.sqrt(number))
print("Square Root of your number is",format(result,".2f"))