class emp():
    sal = 1200000
    language = "py"
    
    @staticmethod
    def greet():
        print("Hello! Good morning.")
        # the dunction is marked as static so it can pass display normal data without self
    
    def getInfo(self):
        print(f"Salary: {self.sal}\nLanguage: {self.language}")


shail = emp()
shail.greet()
shail.getInfo()