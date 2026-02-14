'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
'''

p1 = ("Make a lot of money")
p2 = ("buy now")
p3 = ("subscribe this")
p4 = ("click this")

data = input("enter your comment: ")

if((p1 in data) or (p2 in data) or (p3 in data) or (p4 in data)):
    print("spam")
else:
    print("not spam")

