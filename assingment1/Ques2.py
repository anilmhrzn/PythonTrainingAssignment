# Write a Python code to calculate Combination (15,3)

# importing math
import math

# initializing
n = 15
r=3
nr= n-r

#factorial of n
n = math.factorial(n)   

# factorial of r
r = math.factorial(r)   

# factorial of nr
nr= math.factorial(nr)  

# formula of combination
combination=int(n/(r*(nr)))

# output
print(combination)