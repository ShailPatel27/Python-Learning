with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t3.txt", "r") as f:
    data = f.read()
    
newData = data.replace("Donkey", "######")

with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t3.txt", "w") as f:
    f.write(newData)