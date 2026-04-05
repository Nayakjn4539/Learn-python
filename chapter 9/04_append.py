# a is used to add lines
 
f = open(r"chapter 9/files/file.txt", "a") # a is used because it tells te code to add lines

txt = "he needs a replissage"
f.write(txt)

#cant use read line until the append function is over as the reading head is stuck at the end trying to add to mentioned file.

f.close()

# w is used to write in a file, it will overwrite the existing content
# a is used to append in a file, it will add the content to the existing content
# r is used to read a file, it will read the content of the file
# x is used to create a file, it will create a file if it does not exist
# + is used to open a file in read and write mode
# t is used to open a file in text mode
# b is used to open a file in binary mode
# rb is used to read in binary
# rt is used to read in text