try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)

else:
    print("Program run successfully")   # This will only run when try is completed successfully without going into except