# 7. Write a program to find out whether a given post is talking about “Krishna” or not.
post = input("Enter a post: ")
if "Krishna".lower() in post.lower():
    print("The post is talking about Krishna.")
else:
    print("The post is not talking about Krishna.")