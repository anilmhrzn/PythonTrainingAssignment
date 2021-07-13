# Write a program to check if the number is Armstrong or not.
import math
number=int(input("Enter a number to check wether a number is armstrong or not:"))
temp=number
arm=0
while (number>0):
    rem=number%10
    arm=arm+pow(rem,3)
    number=int(number/10)
   
if (arm==temp):
    print("It is armstrong.")
else:
    print("It is not a armstorng.")
