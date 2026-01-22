# Can we have a set with 18 (int) and '18' (str) as a value in it?
s = (18, "18")

print (type(s))

for element in s:                        #cmd used to pront type of elements in a set
    print ({element}, type(element))


#Answer: yes we can have.