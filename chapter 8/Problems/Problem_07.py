# Write a python function to print multiplication table of a given number

def mult(dig, stnum, endnum): 
        for i in range(stnum, endnum+1):
            print(f"{dig} * {i} = {dig * i}")

dig = int(input("Enter the number whose multiple you wish to find: "))
stnum = int(input("Enter the start number of multiplication table: "))
endnum = int(input("Enter the end number of multiplication table: "))

mult(dig, stnum, endnum)

# another way

def mutiply(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

mutiply(5)