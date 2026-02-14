'''Write a program to greet all the person names stored in a list 'l' and which starts
with S or s.
l = ["Harry", "Soham", "Sachin", "Rahul", "sukanth"]'''

l = ["Harry", "Soham", "Sachin", "Rahul", "sukanth"]

for item in l:
    if item.lower().startswith("s"):
        print(f"greetings {item}")
        
        
for item in l:
    if item.startswith("S" or "s"):    # won't return desired result,  a tupple like ("S","s") will return perfect results.
        print(f"greetings {item}")