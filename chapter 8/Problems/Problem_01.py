# Write a program using functions to find greatest of three numbers

A = int(input("Enter the First Number: "))
B = int(input("Enter the Second Number: "))
C = int(input("Enter the Thrid Number: "))

def greatest():
    if A > B > C :
        return(f"the greatest number is {A}")
    elif B > A > C :
        return(f"the greatest number is {B}")
    else:
        return(f"the greatest number is {C}")

grt = greatest()

print(f"From the numbers you have given {grt}")


# another way to do this 

def greatest(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>b and c>a):
        return c 

a = int(input("Enter Number one: "))
b = int(input("Enter Number two: "))
c = int(input("Enter Number three: "))

print(f"the greatest number is {greatest(a,b,c)}")

        
