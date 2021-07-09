
# A = [‘a’,’b’,’c’,’d’] B = [‘1’,’a’,’2’,’b’]


# for union
common=[]       #this is for intersection
A=['a','b','c','d']
B=['1','a','2','b']
# this is loop for finding common of both list
for common_A in A:
        for common_B in B:
                if common_A == common_B:
                        common.append(common_A)
print('Intersection of A and B is:')
print(common)
#this is for removing the common elemen in one of the list
for union in common:
        A.remove(union)
A.extend(B)
print('\n\nUnion of A and B is:')
print(A)