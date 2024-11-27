#typing does not affect the code
from typing import List, Tuple, Dict, Union

# list of integers
numbers: List[int] = [1, 2,  3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Shail, 30")

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Shail": 30, "Raj": 10}

#Union type for variables that can hold multiple types
a: Union[int, str] = "shail"
a = 10
A = 3.4     #This wont give any error
