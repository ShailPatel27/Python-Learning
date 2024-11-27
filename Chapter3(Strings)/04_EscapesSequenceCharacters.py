a = "PYTHON IS FUN!\nLET'S \"LEARN PYTHON\" \tPROGRAMMING."
print(a)

# Demonstrate escape sequences in a raw string
print("Escape Sequence Characters Example:")

# \n: Newline
print("This is the first line.\nThis is the second line.")

# \t: Horizontal tab
print("Column 1\tColumn 2\tColumn 3")

# \': Single quote
print('It\'s a beautiful day!')

# \": Double quote
print("He said, \"Python is fun!\"")

# \\: Backslash
print("This is a backslash: \\")

# \b: Backspace (removes the character before it)
print("Oops, typo\b!")

# \r: Carriage return (moves the cursor to the beginning of the line)
print("Python programming\rJava")

# \f: Form feed (moves the cursor to the next page in some printers)
print("Hello\fWorld")

# \v: Vertical tab (moves the cursor down vertically, typically unsupported by modern consoles)
print("Vertical\vTab\vExample")

# \N{name}: Unicode character by name
print("Unicode name: \N{COPYRIGHT SIGN}")

# \u: Unicode character by 16-bit hex value
print("Unicode hex: \u00A9")

# \U: Unicode character by 32-bit hex value
print("Unicode hex 32-bit: \U0001F600")  # Smiley face emoji

# \000: Octal value character
print("Octal value character: \101")  # 'A' in octal

# \xhh: Hexadecimal value character
print("Hexadecimal value character: \x41")  # 'A' in hexadecimal
