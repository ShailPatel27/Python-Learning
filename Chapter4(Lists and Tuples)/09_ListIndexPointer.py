# In python, if we change index of a list which is assigned to another variable, then the original will also be changed because it is not assigned to another block of memory but a pointer is pointed to the original.

a = [1,2,3,4,5,6,7,8,9]     # original
b = a   # duplicate
b[0] = 30   # value will be changed for both lists
print(a)