#question: Write a program to input eight numbers from the user and display all the unique
#          numbers (once).

s = set()
n = input("enter number 1: ") # user input accepted as string
s.add(int(n))    # convert user input to integer before importing to set
n = input("enter number 2: ")
s.add(int(n))
n = input("enter number 3: ")
s.add(int(n))
n = input("enter number 4: ")
s.add(int(n))
n = input("enter number 5: ")
s.add(int(n))
n = input("enter number 6: ")
s.add(int(n))
n = input("enter number 7: ")
s.add(int(n))
n = input("enter number 8: ")
s.add(int(n))

print(s)