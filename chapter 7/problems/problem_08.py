'''Write a program to print the following star pattern:
*
**
*** 
for n = 3'''

n = int(input("enter the number here: "))

for i in range(1, n+1):
    print(f"*" * i)
    