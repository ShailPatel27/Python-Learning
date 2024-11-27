try:
    a = int(input("Enter a number: "))  # If we write a string, it will not crash the program
    print(a)

except Exception as e:
    print(e)

print("Done!")  # If not handled with exception, it will not print this line and the program will crash

try:
    a = 2/0
except ZeroDivisionError as ex:
    print(ex)