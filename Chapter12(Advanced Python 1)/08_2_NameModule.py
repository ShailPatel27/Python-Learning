def myFunc():
    print("Hello, world!")

myFunc()

if(__name__ == "__main__"):
    print(f"Program is run from source file ({__name__})")
else:
    print(f"program is run from another file ({__name__})")