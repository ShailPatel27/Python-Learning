class Employee:
    
    @property
    def name(self):
        return f"First Name: {self.fname} \nLast Name: {self.lname}"    #This takes input(maybe?)

    @name.setter
    def name(self, value):  # Name is split into 2 parts and is put into list "value"
        self.fname = value.split(" ")[0]    # 0th index of list ("Shail")
        self.lname = value.split(" ")[1]    # 1st index of list ("Patel")

e = Employee()
e.name = "Shail Patel"
print(f"First Name: {e.fname} \nLast Name: {e.lname}")