a = 10

def myFunc():
    a = 20  # this wont change the value of a outside function since it is a local variable
    print(a)
    
myFunc()
print(a)