'''Write a program to print multiplication table of a given number using for loop.'''

x = int(input("enter the number here; "))


for i in range(0,11):
    print(i*x)
     # i += 1  --> not needed here. its only used in for loops
    
    
# an even better representation goes like this. 

ul = int(input("from which multiple: "))  # asks user to input first multiple
ll = int(input("which multiple: ")) + 1   # asks user to input last multiple
for i in range(ul, ll):
    print(f"{x} X {i} = {x*i}")
    # i += 1  --> not needed here. its only used in for loops