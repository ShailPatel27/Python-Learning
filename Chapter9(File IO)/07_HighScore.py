import random
def game():
    score = random.randint(1, 100)
    print("Your Score: ", score)
    
    with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\highscore.txt") as f:
        highscore = f.read()
        
    if(highscore != ""):
        highscore = int(highscore)
    else:
        highscore = 0
    
    if(score>highscore or highscore == ""):
        print("New High Score!")
        
        with open("F:\\Python\\codewithharry\\Chapter9(File IO)\\highscore.txt", "w") as f:
            f.write(str(score))
    
    return score

game()