from functools import reduce

# Map
l = [1, 2, 3, 4, 5]

square = lambda x: x*x
sqList = map(square, l)     # maps square function and list to get square of elements
print(list(sqList))

# Filter
def even(n):
    if(n % 2 == 0):
        return True
    return False

onlyEven = filter(even, l)  # filters only even elements from the list
print(list(onlyEven))

# Reduce
def sum(a, b):
    return a+b

print(reduce(sum, l))   # sums all elements in list