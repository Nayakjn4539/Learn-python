a = (1, 45, 342, 3424, False, "Rohan", 342, 3424)
print(a)
no = a.count(342)
# counts number of times 342 is present in tupple a
print("number of times 342 is present in tupple a is", no)
i = a.index(3424)
# gives index of first occurence of 3424 in tupple
print("index of first occurence if 3424 in tupple a is", i)
# gives index of first occurence of 3424 in tupple starting from index 3
i = a.index(3424, 3) #look for 3424 after starting from index 3
print("index of frist occurenece of 3424 starting from index 3 in tuuple a is", i)
# assigns index of first occurence of 342 in tupple to variable y
y = index = a.index(342)
print(y)
# assigns index of first occurence of 342 in tupple starting from index 3 to variable y2
y2 = index = a.index(342, 3)
print(y2)
l = len(a)
print("length of tupple a is", l)

w, x, y, z, p, q, r, s = a
print(w, x, y, z, p, q, r, s)

t = type("Rohan")
print(t) #prints type of variable t