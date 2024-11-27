with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t1.txt") as f:
    data = f.read()
    
with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t1_copy.txt", "w") as f:
    f.write(data)