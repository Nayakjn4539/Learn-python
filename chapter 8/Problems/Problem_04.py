'''
Write  a python function to print first n lines of the following pattern
***
**
*
for n=3
'''

'''
so given is 
n * {"*"}
(n-1) * {"*"}
(n-2) * {"*"}
...
n = 0
'''

def pat(n):
    if (n == 0):
        return
    print(n * "*")
    pat(n-1)

n = int(input("enter number of rows: "))
pat(n) 

# if ptint(pat(n)) then it will print None after the pattern whuich we dont want
