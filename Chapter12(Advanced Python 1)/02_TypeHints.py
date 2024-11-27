#Only used to display the type of variable, it does not make it 
#Useful for multiple developers working on the same code
n : int = 5
# n.    will display all int operations

name : str = "Shail"

def sum(a: int, b: int) -> int:     #-> is used to display return type. For example public int main will return int. Similarly -> int will return int in python.
    return a+b

print(sum(10, 20))