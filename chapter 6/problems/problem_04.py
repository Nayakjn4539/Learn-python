'''Write a program to find whether a given username contains less than 10
characters or not.'''

name = input("enter the name: ")

if(len(name)<10):
    print("the numebr of letters in the name is less than 10")
else:
    print("exceeded character limit")