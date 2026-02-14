''''goal is ot print numebrs from 1 to 1000.
an inexperienced guy would do it like this:- '''

print(1)
print(2)
print(3)
'''and so on until print(1000). this is impractical. hence loops are used'''

#the most efficient way is
for i in range(1,1000): #wont print the last number as it is exclusive at stop k/a upper bound exclusive
    print(i)
