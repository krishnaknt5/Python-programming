#7. Write a program to find out the line number where python is present from ques 6. 
# This code finds the line number(s) where the word 'python' appears in a log file named 'log.txt'.
line = 1
with open('log.txt', 'r') as f:
        line = f.readlines()
lineno=1
for line in line:
        if 'python' in line:
            print(f"yes python is present. Line no:{lineno}")
            break # If you want to find all occurrences, remove the break statement 
              # the else will execute only if the loop completes without finding 'python'
        lineno += 1

else:
            print("no python is present.")