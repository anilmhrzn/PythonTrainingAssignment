# Write a program to compute the grade from marks. 

# Marks
# Grade
# Marks<=50
# F
# 60>=marks>50
# E
# 70>= marks > 60
# D
# 80>= marks > 70
# C
# 90 > = marks > 80
# B
# 100>= marks >90
# A

m1=int(input("Enter marks in first subject:\t"))
m2=int(input("Enter marks in second subject:\t"))
m3=int(input("Enter marks in third subject:\t"))
m4=int(input("Enter marks in fourth subject:\t"))
m5=int(input("Enter marks in fifth subject:\t"))
percentage=(m1+m2+m3+m4+m5)/5
if (percentage<=50):
    print('Your grade is F')
elif(percentage>50 and percentage<=60):
    print('Your grade is E')
elif(percentage>60 and percentage<=70):
    print('Your grade is D')
elif(percentage>70 and percentage<=80):
    print('Your grade is C')
elif(percentage>80 and percentage<=90):
    print('Your grade is B')
elif(percentage>90 and percentage<=100):
    print('Your grade is A')
