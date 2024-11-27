n = int(input("Enter a number: "))
# a number is only prime when it is either divided by 1 or by itself

for i in range(2, n):   #1 & 2 are prime
    if(i%n == 0):       #loop will go till n-1
        print("Number is not prime")
        break
else:   # this is executed when the loop is completed entirely (since there was no break, else will be executed so no need for flag)
    print("Number is prime")