#recursive function that calculates sum of N natural numbers

'''
Formula= n(n+1)/2
'''

def sum(n):
    return n * (n+1)//2

n = int(input("Enter a number: "))

print(f"The sum of {n} natural numbers is {sum(n)}") 

#Another Method

def all(n):
    if(n==1):
        return 1
    return all(n-1) + n

print(all(4))