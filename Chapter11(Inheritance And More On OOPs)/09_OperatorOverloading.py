class abc:
    
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):
        return self.n + num.n
        
x = abc(10)
y = abc(20)

print(x+y)  #directly add classes
print(type(x))