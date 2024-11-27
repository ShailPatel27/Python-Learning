# Initialize a sample dictionary
student = {
    "name": "Alice",
    "age": None,
    "subjects": ["Math", "Science"],
    "grade": "A"
}

print("Original dictionary:", student)

# 1. get(): Get the value of a specified key
name = student.get("name")
print("Name:", name)

# 2. keys(): Get all keys in the dictionary
keys = student.keys()
print("Keys:", keys)

# 3. values(): Get all values in the dictionary
values = student.values()
print("Values:", values)

# 4. items(): Get all key-value pairs as a list of tuples
items = student.items()
print("Items:", items)

# 5. update(): Update dictionary with another dictionary
student.update({"age": 21, "major": "Physics"})
print("After update:", student)

# 6. pop(): Remove an element with a specific key and return its value
age = student.pop("age")
print("Removed age:", age)
print("After pop('age'):", student)

# 7. popitem(): Remove the last inserted key-value pair
last_item = student.popitem()
print("Removed last item:", last_item)
print("After popitem():", student)

# 8. setdefault(): Get the value of a key if it exists; if not, insert the key with a specified value
grade = student.setdefault("grade", "B")
print("Grade:", grade)
print("After setdefault('grade', 'B'):", student)

# 9. clear(): Remove all items from the dictionary
student.clear()
print("After clear():", student)

# 10. copy(): Create a shallow copy of the dictionary
new_student = {"name": "Bob", "age": 22, "grade": "B"}
student_copy = new_student.copy()
print("Copied dictionary:", student_copy)