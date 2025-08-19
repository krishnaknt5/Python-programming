'''3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 - year old. '''

# This code generates multiplication tables from 2 to 20 and writes them to separate files in a 'tables' directory.
def generateTable(n):
    table=""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    with open(f'tables/table_{n}', 'w') as f:
        f.write(table)
# Create a directory named 'tables' if it doesn't exist
for i in range(2, 21):
    generateTable(i)





    #for this program i created a function named generateTable which takes a number as an argument and generates the multiplication table for that number from 1 to 10.
# The function writes the table to a file named 'table_<number>' in a directory named 'tables'.
# The program then calls this function for numbers from 2 to 20, creating a separate file for each multiplication table.
# The files are stored in a directory named 'tables' which should be created beforehand.
#i created a file named 'tables' in which all the tables will be stored