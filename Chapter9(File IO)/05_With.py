f = open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t1.txt")
print(f.read())
f.close()

print("\n")

#in with statement, you dont need to use f.close()
with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t1.txt") as f:
    print(f.read())
    
#file will automatically close when the indentation is completed    