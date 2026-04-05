data = "A replissage might be needed for Jignesh's healing"

f = open(r"chapter 9/files/file.txt", "w") # this will delete existing data and rewrite here
f.write(data)
f.close()

# w is used to write in a file, it will overwrite the existing content
# a is used to append in a file, it will add the content to the existing content
# r is used to read a file, it will read the content of the file
# x is used to create a file, it will create a file if it does not exist
# + is used to open a file in read and write mode
# t is used to open a file in text mode
# b is used to open a file in binary mode 