# Write a Python code to calculate LCM of (25,55)
num1, num2 = 25, 55

# To  choose the greater number
if (num1 > num2):
    greater = num1
else:
    greater = num2

while(True):
    # To find LCM
    if(greater % num1 == 0 and greater % num2 == 0):
        print('The LCM of', num1, 'and', num2, 'is', greater)
        break
    greater += 1
