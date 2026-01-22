s1 = {1, 3, 4, 5}
s2 = {6, 7, 9, 11, 3, 4, 5}
s3 = {3, 5, 6, 7, 8, 9, 4}

print(s1.union(s2))#combines multiple sets(of course no duplicate characters)
print(s1.intersection(s2))#return only the common elements in 2 sets
print(s1.intersection(s2,s3))#returns common elements of 3 sets