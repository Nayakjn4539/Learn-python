name = "Jignesh"
# strings are immutable i.e. they can't be changed once they are formed

lettersinname = len(name)#llen prints the nukber of letters or the length of the string
print(lettersinname)

# start from index and go from 0th charcater to 2nd character
nameshort = name[0:3]
print(nameshort)

# negaticve slicing
# numbering in negative starts from -1 and moves backwards
letter1 = name[-5:-1]
print(letter1)

print(name[:6])  # same as [0:6]
print(name[0:])  # same as [0:7] oit prints the whole name

a = "0123456"
print(a)
# skip values
print(name[2:7:2])  # this works like [ start:stop:skip] start digit then skipeth digit is printed

print(name.endswith("esh"))
print(name.startswith("jign"))#case sensitive
print(name.startswith("Jign"))#case sensitive
print(name.capitalize())#capitalize first letter
print(name.upper())

