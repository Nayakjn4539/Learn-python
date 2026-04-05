'''
Write a program to read the text from a given file 'poems.txt' and find out
whether it contains the word 'twinkle'.
'''

input_path = r"D:\learn python\chapter 9\problems\poem.txt"
f = open(input_path)
content = f.read()
ser_data = input("Eneter the word you wish to find: ")
if(ser_data.lower() in content.lower()): #reduces everything ot lowercase so it becomes easier to match user input with capital letters
    print(f"The Given word {ser_data} is present in given {input_path}")
else:
    print(f"Given word {ser_data} is not present in the given file located at {input_path}")
f.close()
