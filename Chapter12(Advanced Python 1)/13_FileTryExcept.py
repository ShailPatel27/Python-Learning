try:
    with(
        open("F:\\Python\\codewithharry\\Chapter12(Advanced Python 1)\\13_file1.txt", "r") as f1,
        open("F:\\Python\\codewithharry\\Chapter12(Advanced Python 1)\\13_file2.txt", "r") as f2,
        open("F:\\Python\\codewithharry\\Chapter12(Advanced Python 1)\\13_file3.txt", "r") as f3
    ):
        print(f1.read())
        print(f2.read())
        print(f3.read())
        
except FileNotFoundError as e:
    print(e)
    
print("Done!")