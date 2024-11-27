import random
num = random.randint(0, 100)
score = 0

def guessNumber():
    global score
    user = int(input("Guess a number between 0 and 100: "))
    if(user == num):
        return f"You Won! \nScore: {score}"
    else:
        if(user > num):
            print("Wrong Guess! Go Lower")
        elif(user < num):
            print("Wrong Guess! Go Higher")
            
        score = score + 1
        return guessNumber()

print(guessNumber())