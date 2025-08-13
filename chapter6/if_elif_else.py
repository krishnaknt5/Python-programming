# it is about if_elif_else laddder
a=int(input("Eneter your age "))
if(a>=18):
    print("you are above age of consent")
    print("you can vote")
elif(a<0):
    print("you are entering inavlid age")
elif(a==0):
    print("you are entering 0")
else:
    print("you are bilow age of consent")
    print("you cant vote")
print("End of program")