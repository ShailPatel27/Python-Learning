class superClass:
    a = 10
    
class subClass(superClass):
    a = 20
    
    def display(self):
        print(f"Value of a in super class: {super().a}")    #needs self to be imported
        print(f"Value of a in sub class: {self.a}")
        
x = subClass()
x.display()