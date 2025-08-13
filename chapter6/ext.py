a=int(input("Eneter your age "))
if(a%2==0):
    print("a is even")

#there  is no relation between these 2 if ststements both are independent

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