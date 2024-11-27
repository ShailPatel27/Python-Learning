def hello(name, ending):
    print(f"Hello {name}!")
    print(f"{ending} {name}")
    
    return "done👍"

name = input("Enter your name: ")
a = hello(name, "Goodbye")
print(a)