n = int(input("Enter number: "))

fact = 1
for i in range(n, 1, -1):
    fact = fact * i
    
print(f"Factorial of {n} is: {fact}")