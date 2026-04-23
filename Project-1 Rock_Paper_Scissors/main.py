import random

while True:
    
    youTotal = 0
    compTotal = 0

    matchesCount = int(input("Enter Match Count: "))

    for i in range(0, matchesCount):
        
        dict = {-1: "Rock🪨", 0: "Paper📃", 1: "Scissors✂️"}
        revDict = {"r": -1, "p": 0, "s": 1}

        comp = random.choice([-1, 0, 1])

        youStr = input("Enter your choice(R, P, S): ")
        you = revDict.get(youStr.lower())

        print(f"You Chose: {dict.get(you)}")
        print(f"Computer Chose: {dict.get(comp)}")

        if(you == comp):
            print("It's a Draw!")
        else:
            if(you == -1 and comp == 0):
                print("You Lose!")
                compTotal += 1
            elif(you == -1 and comp == 1):
                print("You Win!")
                youTotal += 1
            elif(you == 0 and comp == -1):
                print("You Win!") 
                youTotal +=1
            elif(you == 0 and comp == 1):
                print("You Lose!")
                compTotal += 1
            elif(you == 1 and comp == -1):
                print("You Lose!")
                compTotal += 1
            elif(you == 1 and comp == 0):
                print("You Win!")
                youTotal +=1
            else:
                print("Something Went Wrong")
                
    if(youTotal > compTotal): print("You Win")
    elif (compTotal < youTotal): print("Youe Lose!")
    else: print("It's a Draw ")
    print(f"Your Score: {youTotal}")
    print(f"Your Score: {compTotal}")
    
    again = input("Play Again? (y) (n) ")


    if(again != "y" or again != "Y"):
        break