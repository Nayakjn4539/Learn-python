'''Write a program which finds out whether a given name is present in a list or not.'''

n_1 = input("enetr name 1: ")
n_2 = input("enter name 2: ")
n_3 = input("enter naem 3: ")
n_4 = input("enter name 4: ")

name_list = [n_1, n_2, n_3, n_4]

if("harry" in name_list):
    print("harry is permitted")
else:
    print("harry is not permitted")