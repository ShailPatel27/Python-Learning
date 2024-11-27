class emp():
    sal = 1200000
    language = "py"
    
    def __init__(self, name, sal, language):
        self.name = name
        self.sal = sal
        self.language = language
    
        print("This is a constructor in python")

    @staticmethod
    def greet():
        print("Hello! Good morning.")
    
    def getInfo(self):
        print(f"Name: {self.name}\nSalary: {self.sal}\nLanguage: {self.language}")

shail = emp("Shail", 10000, "JS")
shail.greet()
shail.getInfo()