#Used to Mark variables to a specific type. It shows that the variable n is now an integer whether it is or isnt doesnt matter; the developer marked it as such.
n : int = 5
# now n. suggestion box will display all int operations

name : str = "Shail"

def sum(a: int, b: int) -> int:     # "->" is used to display return type. For example public int main will return int. Similarly -> int will return int in python.
    return a+b

print(sum(10, 20))