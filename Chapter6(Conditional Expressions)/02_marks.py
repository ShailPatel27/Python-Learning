marks1 = int(input("Enter marks of English: "))
marks2 = int(input("Enter marks of Maths: "))
marks3 = int(input("Enter marks of Science: "))

total_percentage = ((marks1 + marks2 + marks3)/300) *100

if(total_percentage >= 40):
    if(marks1>33 and marks2>33 and marks3>33):
        print("You passed!")
    else:
        print("You Failed In One Or More Subjects")
else:
    print("You Failed!")
