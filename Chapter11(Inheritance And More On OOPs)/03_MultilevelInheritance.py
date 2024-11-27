class a:
    a = 10
    
    def displaya(self):
        print("Value of a: ", self.a)

class b(a):     #Multilevel Inhertance
    b = 20
    
    def displaya(self):
        print("Value of b: ", self.b)
        
class add(b):     #Multilevel Inhertance
    
    def displaySum(self):
        print("Addition of both numbers is: ", (self.a+self.b))
        
x = add()
x.displaySum()