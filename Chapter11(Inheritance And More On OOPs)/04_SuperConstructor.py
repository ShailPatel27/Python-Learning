class superClass:
    def __init__(self):
        print("Constructor of super class")
        
class subClass(superClass):
    def __init__(self):
        print("Constructor of sub class")
        super().__init__()
        
x = subClass()