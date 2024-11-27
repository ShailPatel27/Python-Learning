class emp():
    sal = 1200000
    language = "py"
    
    # methods starting with "__" are called dunder method
    def __init__(self): #dunder method which is automatically called
        print("This is a constructor in python")

    @staticmethod
    def greet():
        print("Hello! Good morning.")
        # the dunction is marked as static so it can pass display normal data without self
    
    def getInfo(self):
        print(f"Salary: {self.sal}\nLanguage: {self.language}")


shail = emp()
shail.greet()
shail.getInfo()