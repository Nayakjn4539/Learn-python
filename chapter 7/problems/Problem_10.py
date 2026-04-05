'''Write a program to print multiplication table of a given number using for loop. the program must account for the case when the user enters the end of the table before the start of the table'''

x = int(input("enter the number whose table you need: "))

m1 = int(input("enter the start of the multiplication table: "))
m2 = int(input("enter the end of the mutiplication table: "))


if m1<m2:
    for i in range(m1, m2+1):
        print(f"{x} X {i} = {x*i}")
elif m1>m2:
    for i in range (m1, m2-1, -1):
        print(f"{x} X {i} = {x*i}")
else:
    print("Input issue is found")


 