#python lists are container to store any data type
#lists are mutable unline strings
friends = ["jignesh", "apple", "sailesh", 5, 345.06, False, "mukesh"]
print(friends[0:6])#indexing is similar to indexing in strings
t = type(friends[0])
friends[0] = "grapes"#unlike strings lisst are mutable
print(t)
for item in friends:#for assigns the objects in container to item temporarily
 print(f"{item}, {type(item)}")
 