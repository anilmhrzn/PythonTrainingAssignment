# Write a python program to find the largest of three numbers .
firstnumber = int(input("Enter first number."))
secondnumber = int(input("Enter second number."))
thirdnumber = int(input("Enter third number."))
if firstnumber > secondnumber and firstnumber > thirdnumber:
    print("{} is the greatest number.".format(firstnumber))
elif secondnumber > firstnumber and secondnumber > thirdnumber:
    print("{} is the greatest number.".format(secondnumber))
else:
    print("{} is the greatest number.".format(thirdnumber) )
