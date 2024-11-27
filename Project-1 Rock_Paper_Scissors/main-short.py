import random

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
    if((-you + comp == -1) or (-you + comp == 2)):
        print("You Win!")
    else:
        print("You Lose!")
        
    #               ADVANCED ANALYSIS:
    # THINK OF VARIOUS COMBINATIONS TO SHORTEN YOU CODE
    # if(you == -1 and comp == 0):      (-(-1) + 0  ) = 1
    #     print("You Lose!")
    # elif(you == -1 and comp == 1):    (-(-1) + 1) = 2
    #     print("You Win!")
    # elif(you == 0 and comp == -1):    ((-0) + -1) = -1
    #     print("You Win!")
    # elif(you == 0 and comp == 1):     ((-0) + 1) = 1
    #     print("You Lose!")
    # elif(you == 1 and comp == -1):    ((-1) + -1) = -2
    #     print("You Lose!")
    # elif(you == 1 and comp == 0):     ((-1) + 0) = -1
    #     print("You Win!")