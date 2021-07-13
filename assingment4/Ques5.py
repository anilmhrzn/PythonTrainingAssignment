# Write a program to check whether the entered year is leap year or not.
year=int(input("Enter a year:\t"))
if year%4==0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")