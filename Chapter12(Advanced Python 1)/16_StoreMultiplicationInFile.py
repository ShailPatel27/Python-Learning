import importlib
m = importlib.import_module("15_ListComprehensionMultiplication")
table = m.mulFun()

# Program will run twice. First input will be asked for imported file and second input will be asked for current file

with open("F:\\Python\\codewithharry\\Chapter12(Advanced Python 1)\\16_tables.txt", "w") as f:
    f.write(str(table))
    print("Table Created")