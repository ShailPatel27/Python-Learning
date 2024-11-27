with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\t5.txt") as f:
    lines = f.readlines()

    lineNo = 1
    for line in lines:
        if("Python" in line):
            print(f"Python is present at Line number: {lineNo}")
            break
    
        lineNo += 1

    else:
        print("Python is not present")