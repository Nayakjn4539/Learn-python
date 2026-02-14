'''Attempt problem 1 using while loop.'''
'''problem 1: Write a program to print multiplication table of a given number using for loop.'''

i = int(input("enter number whose multiples are needed: "))

l = int(input("enter last multiple needed: "))

n = 0
while(n < l):
    print(f"{i} X {n} = {i * n}" )
    n += 1   # removing this line will cause infinite loop problem