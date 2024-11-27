words = ["free", "buy now", "click this"]

with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t4.txt", "r") as f:
    data = f.read()

for i in words:    
    data = data.replace(i, "#" * len(i))

with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t4.txt", "w") as f:
    f.write(data)