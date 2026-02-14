'''Write a program to calculate the factorial of a given number using for loop.'''

# factorial of 4 = 4 X 3 X 2 X 1
n = int(input("enter the number whose factorial is needed: "))

product = 1
for i in range(1, n+1):
    product = product * i
print(f"{n}! = {product}") # think why this is not intended


