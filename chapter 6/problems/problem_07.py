'''Write a program to find out whether a given post is talking about “Harry” or not.'''

post = input("enter the text here: ")

if("harry" in post.lower()):
    print("post is indeed about harry")
else:
    print("post not talking about harry")