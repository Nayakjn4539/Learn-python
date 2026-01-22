name = input("enter your name: ")
date = input("Today's date: ")
print(f"Dear {name} \nyou are selected \n{date}")

#another method
data = '''Dear Name
You have won!
<|Date|>
a cash prize of <|amount>|'''
b = input("enter amount needed: ")
#.replace finds that particualr sequemce and replaces it with defined variable
print(data.replace("Name", name).replace("<|Date|>", date).replace("<|amount>|", b))
