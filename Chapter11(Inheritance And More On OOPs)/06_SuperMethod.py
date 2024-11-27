class superClass:

    def display(self):
        print("This is super class")
        
class subClass(superClass):

    def display(self):
        print("This is sub class")
        
    def printSuper(self):
        super().display()
        
x = subClass()
x.printSuper()
x.display()