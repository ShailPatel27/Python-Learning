class emp():
    sal = 1200000
    language = "py"


shail = emp()
shail.language = "JavaScript"    #instance attribute
print(shail.sal, shail.language)
#instance attribute takes priority over class attribute