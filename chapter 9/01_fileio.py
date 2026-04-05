'''
a = "a very long string with emails"

emails = [] 
3 seconds
'''

f = open(r"chapter 9/files/file.txt") # r is used to mention file path, if no path i.e no slash then no need of r
# if file name has spaces then use r
data = f.read()
print(data)
f.close()