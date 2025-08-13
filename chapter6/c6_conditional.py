#chapter 6 is about conditions in python
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

#in the above program the spaces after if and else statements are called indentiation which means we are inside the particular condition
#if condition is true means else will never print