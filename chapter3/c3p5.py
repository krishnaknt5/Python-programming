#5. Write a program to format the following letter using escape sequence characters. 
letter = "Dear lucky, \n\tYou r a good guy,\n I hope you are doing well.\nThanks for helping us!\n\tByy" 
print(letter)

#the above program uses escape sequences like \n for new line and \t for tab space to format the letter. 

# print(letter.replace("lucky", "Krishna").replace("good", "nice")) but this is not needed as the letter is already formatted with escape sequences.
#according to the problem statement, print(letter.replace("lucky", "Krishna") may can use to replace the name lucky with Krishna, but it is not needed as the letter is already formatted with escape sequences.