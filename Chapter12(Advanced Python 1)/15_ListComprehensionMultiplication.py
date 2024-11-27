def mulFun():
    num = int(input("Enter a number: "))    

    table = [num*i for i in range(1, 11)]
    return table

print(mulFun())