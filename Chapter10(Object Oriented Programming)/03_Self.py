class emp():
    sal = 1200000
    language = "py"
    
    def greet(self):
        print("Hello! Good morning.")
        # need to pass self to display or write anything
    
    def getInfo(self):
        print(f"Salary: {self.sal}\nLanguage: {self.language}")
        # kinda works like "this" keyword but you have to put it as a paramerer


shail = emp()

shail.getInfo()

# can also be written as:
# emp.getInfo(shail)