class calculator():

    def __init__(self, num):
        self.num = num

    def sq(self):
        print("Square of number: ", self.num*self.num)
        
    def cube(self):
        print("Cube of number: ", self.num*self.num*self.num)

    def sqroot(self):
        print("Square root of number: ", self.num**(1/2))

num = int(input("Enter number: "))

a = calculator(num)
a.sq()
a.sqroot()
a.cube()
        