a = 10

def myFunc():
    global a    #This refers to the a outside of the function
    a = 20      # This will change the value of a outside function to 20
    print(a)
    
myFunc()
print(a)