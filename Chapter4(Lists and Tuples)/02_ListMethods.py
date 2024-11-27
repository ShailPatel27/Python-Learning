# Initialize a sample list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# 1. append(): Add an element to the end of the list
numbers.append(60)
print("After append(60):", numbers)

# 2. extend(): Add multiple elements to the end of the list
numbers.extend([70, 80])
print("After extend([70, 80]):", numbers)

# 3. insert(): Insert an element at a specific index
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

# 4. remove(): Remove the first occurrence of a specific element
numbers.remove(30)
print("After remove(30):", numbers)

# 5. pop(): Remove and return the last element (or an element at a specified index)
popped_element = numbers.pop()
print("After pop():", numbers)
print("Popped element:", popped_element)

# 6. index(): Get the index of the first occurrence of a specific element
index_of_40 = numbers.index(40)
print("Index of 40:", index_of_40)

# 7. count(): Count the occurrences of a specific element
count_of_20 = numbers.count(20)
print("Count of 20:", count_of_20)

# 8. sort(): Sort the list in ascending order
numbers.sort()
print("After sort():", numbers)

# 9. reverse(): Reverse the order of the list
numbers.reverse()
print("After reverse():", numbers)

# 10. copy(): Create a shallow copy of the list
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)

# 11. clear(): Remove all elements from the list
numbers.clear()
print("After clear():", numbers)
