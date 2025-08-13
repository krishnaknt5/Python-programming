# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")
message_lower = message.lower()
if p1.lower() in message_lower or p2.lower() in message_lower or p3.lower() in message_lower or p4.lower() in message_lower:
    print("This message is a spam comment.")
else:
    print("This message is not a spam comment.")
