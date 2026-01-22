# question: Create an empty dictionary. Allow 4 friends to enter their favorite language as
#           value and use key as their names. Assume that the names are unique.

s = {}
n = input("what is your name: ")
lang = input("enter fav language: ")
s.add({n : lang })
n = input("what is your name: ")
lang = input("enter fav language: ")
s.update({n : lang })
n = input("what is your name: ")
lang = input("enter fav language: ")
s.update({n : lang })
n = input("what is your name: ")
lang = input("enter fav language: ")
s.update({n : lang })

print (s)