name = "shail patel"

print(len(name))

print(name.endswith("el"))
print(name.startswith("ab"))
print(name.capitalize())

# Define a sample string
text = "  Python is Fun! Let's learn Python programming.  "

# 1. len(): Get the length of the string
length = len(text)
print(f"Length of the string: {length}")

# 2. lower(): Convert the string to lowercase
lower_text = text.lower()
print(f"Lowercase: {lower_text}")

# 3. upper(): Convert the string to uppercase
upper_text = text.upper()
print(f"Uppercase: {upper_text}")

# 4. strip(): Remove leading and trailing whitespaces
stripped_text = text.strip()
print(f"Stripped: '{stripped_text}'")

# 5. split(): Split the string into a list of words
words = stripped_text.split()
print(f"Words: {words}")

# 6. replace(): Replace a substring with another
replaced_text = stripped_text.replace("Python", "Java")
print(f"Replaced 'Python' with 'Java': {replaced_text}")

# 7. find(): Find the index of the first occurrence of a substring
index = stripped_text.find("Fun")
print(f"Index of 'Fun': {index}")

# 8. join(): Join a list of words with a separator
joined_text = "-".join(words)
print(f"Joined words with hyphen: {joined_text}")

# 9. startswith(): Check if the string starts with a specified substring
starts_with = stripped_text.startswith("Python")
print(f"Starts with 'Python': {starts_with}")

# 10. endswith(): Check if the string ends with a specified substring
ends_with = stripped_text.endswith("programming.")
print(f"Ends with 'programming.': {ends_with}")
