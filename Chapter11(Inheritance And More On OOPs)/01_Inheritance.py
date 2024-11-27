class Employee:
    company = "Google"
    name = "Shail"
    salary = 1000000
    
    def showdetails(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    def showLanguage(self, language):
        print(f"The name is: {self.name} and the Language is: {language}")
        
b = Programmer()
b.showdetails()
b.showLanguage("C++")