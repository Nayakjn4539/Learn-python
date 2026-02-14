'''Write a program to find the sum of first n natural numbers using while loop'''

#method !
n = int(input("numbers upto which you want to sum up"))

sum = (n * (n + 1))/2

i = 0
while(i < n):
    i += 1
print(sum) # observe how it is kept outside the indentation.
    
    
#method 2
n = int(input("Enter the number: "))
i = 1
sum = 0
while(i <= n):
    sum += i
    i += 1

print(sum)