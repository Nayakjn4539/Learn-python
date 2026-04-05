f = open(r"chapter 9/files/file.txt")

#lines = f.readlines()   #reads till completing all lines
#print(lines, type(lines))


line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
line5 = f.readline() # wont do nothing as there is no line 5

print(line1, type(line1))
print(line2, type(line2))
print(line3, type(line3))
print(line4, type(line4))
print(line5, type(line5))



# can do the same thing using whileloop too
f.seek(0)  # resets reading head to shift to file start
study = f.readline()
while(study != ""):
    print(study)
    study = f.readline()



f.close()