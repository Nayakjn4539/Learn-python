f = f.open(r"chapter 9/files/file.txt")
print(f.read())
f.close()

# the same can be written like this by usng with statement
with open("file.txt") as f:
    print(f.read())
    # no need to explicitly close the file. with automatically closes file

