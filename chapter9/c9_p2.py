'''2. The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file 'Hi-score.txt' which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score. '''

import random
def game():
    print("user is playing the game")
    #we made a function named game which prints user is palying game
    #generate a random score for the user between 1 and 111
    
    score = random.randint(1, 111)
    #fetch the previous high score from the file
    with open('Hi-score.txt', 'r') as f:
        #we used Hi-score.txt file to store the high score if it is blank high score is 0 else the highest number generatte by the program wiill be the high score
        #read the content of the file using read() function
        highscore = f.read()
        if(highscore!=""):
            #we convert the high score to an integer if it is not blank as the f.read() function returns a string
            
            highscore=int(highscore)
        else:
            highscore = 0
    print(f"user score:{score}") #print the score of the user
    if(score>highscore):
    #if the score is greater than the high score then we update the high score
        with open('Hi-score.txt', 'w') as f:
            f.write(str(score))
            return score
game()



# the second problem use to print high score which will show in this file only the highest one