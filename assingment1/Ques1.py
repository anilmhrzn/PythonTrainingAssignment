# Write a Python code to calculate Permutation (5,3)
# importing math
import math

# initializing
n=5
r=n-3

# for numerator
numerator= math.factorial(n)

# for denominator
denominator= math.factorial(r)

# finding permutation
permutation = int(numerator/denominator)

# output
print(permutation)