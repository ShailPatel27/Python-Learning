class abc:
    a = 10

    @classmethod    #Class method overrides the instance attribute with class attribute
    def display(cls):
        print(f"The class attribute of a is: {cls.a}")

x = abc()
x.a = 20    #Instance Attribute has the highest priority
x.display()