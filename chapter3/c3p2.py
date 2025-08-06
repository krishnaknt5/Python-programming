#2. Write a program to fill in a letter template given below with name and date. letter = '''  
# letter='''Dear <|Name|>, You are selected! <|Date|> ''' 
letter = '''Dear <|Name|>,
You are selected! 
<|Date|> '''
print(letter.replace("<|Name|>", "Krishna").replace("<|Date|>", "01/01/2023")) 
# This will replace the placeholders with actual values and print the letter.
#letter.replace is used to replace the placeholders with actual values.