'''Group of Statements performing a said task'''

def avg():
    a = int(input("enter the number 1 here: "))
    b = int(input("enter the number 2 here: "))
    c = int(input("enter the number 3 here: "))
    d = int(input("enter the number 4 here: "))
    e = int(input("enter the number 5 here: "))
    return (a+b+c+d+e)/5

b = avg() #Function call

print(f"The Average you need is {b}")