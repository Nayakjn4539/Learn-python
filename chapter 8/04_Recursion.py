# function to generate factorial

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial (n-1) #function calling itself and it keeps doing that till n == 1 or n == 0

n = int(input("Enter a number: "))

print(f"The factorial of {n} is {factorial(n)}")