# Initialize sample sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Original sets:")
print("set_a:", set_a)
print("set_b:", set_b)

# 1. add(): Add a single element to the set
set_a.add(6)
print("After add(6) to set_a:", set_a)

# 2. update(): Add multiple elements to the set
set_a.update([7, 8])
print("After update([7, 8]) to set_a:", set_a)

# 3. remove(): Remove an element from the set (raises KeyError if element not found)
set_a.remove(8)
print("After remove(8) from set_a:", set_a)

# 4. discard(): Remove an element from the set (does nothing if element not found)
set_a.discard(10)  # No error even though 10 is not in set_a
print("After discard(10) from set_a:", set_a)

# 5. pop(): Remove and return an arbitrary element from the set
popped_element = set_a.pop()
print("Popped element:", popped_element)
print("After pop() from set_a:", set_a)

# 6. clear(): Remove all elements from the set
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear() from temp_set:", temp_set)

# 7. union(): Return a new set with all elements from both sets
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# 8. intersection(): Return a new set with elements common to both sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# 9. difference(): Return a new set with elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("Difference of set_a - set_b:", difference_set)

# 10. symmetric_difference(): Return a new set with elements in either set_a or set_b but not both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", symmetric_difference_set)

# 11. issubset(): Check if set_a is a subset of set_b
is_subset = set_a.issubset(set_b)
print("set_a is subset of set_b:", is_subset)

# 12. issuperset(): Check if set_a is a superset of set_b
is_superset = set_a.issuperset(set_b)
print("set_a is superset of set_b:", is_superset)

# 13. isdisjoint(): Check if set_a and set_b have no elements in common
is_disjoint = set_a.isdisjoint(set_b)
print("set_a and set_b are disjoint:", is_disjoint)

# 14. copy(): Create a shallow copy of the set
set_a_copy = set_a.copy()
print("Copy of set_a:", set_a_copy)