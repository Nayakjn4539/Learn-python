a = (1,3,0,50,0,0,50,505,0,50,5,105,50,505,5,5,5,50,50,30,50,32,50,55,2,5,206,7)
n = a.count(0)
print(n)

j = ' '.join(str(item) for item in a)
print (j)
zeros_in_j = j.count('0')
print(zeros_in_j)

