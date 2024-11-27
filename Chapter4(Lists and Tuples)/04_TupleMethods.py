# Initialize a sample tuple
numbers = (10, 20, 30, 20, 40, 20, 50)
print("Original tuple:", numbers)

# 1. count(): Count the occurrences of a specific element
count_of_20 = numbers.count(20)
print("Count of 20 in tuple:", count_of_20)

# 2. index(): Get the index of the first occurrence of a specific element
index_of_30 = numbers.index(30)
print("Index of 30 in tuple:", index_of_30)

# 3. len(): Get the length of the tuple
print(f"Length of tuple: {len(numbers)}")