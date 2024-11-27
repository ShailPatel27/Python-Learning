class abc():
    a = 10
    
o = abc()
o.a = 0
print(o.a)
print(abc.a)

print()

abc.a = 0
print(o.a)
print(abc.a)