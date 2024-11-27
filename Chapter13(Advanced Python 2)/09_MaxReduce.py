from functools import reduce

l = [1, 24, 54, 325, 65, 92]

def max(a, b):
    if(a>b):
        return a
    return b

print(reduce(max, l))