f = open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t1.txt")
data = f.read()
if("Twinkle" in data):
    print("Twinkle found in file")
else:
    print("Not found")