# Write a program to check whether the input alphabet is vowel or not using if-else.
ch = input("Enter a alphabet:\t")
ch=ch.lower()
if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
# if(ch == 'a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
    print('The given alphabet is vowel.')
else:
    print('The given alphabet is consonant.')

