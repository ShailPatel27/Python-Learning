class a:
    a = 10
    
    def displaya(self):
        print("Value of a: ", self.a)

class b:
    b = 20
    
    def displaya(self):
        print("Value of b: ", self.b)
        
class add(a, b):    #Multiple Inhertance
    
    def displaySum(self):
        print("Addition of both numbers is: ", (self.a+self.b)) #Need to include self (@staticmethod won't work)
        
x = add()
x.displaySum()