# # Write a python program to check whether a character is uppercase or lowercase alphabet.
character=input("Enter a character:\t")
if(character.isupper()):
    print("The character you entered is uppercase")
elif(character.islower()):
    print("The character you entered is lowercase")
else:
    print("The charcter you entered is neither lowercase nor uppercase")
