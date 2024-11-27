with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t5.txt") as f:
    data = f.read()

if("Python" in data):
    print("Python is present")
else:
    print("Python is not present")