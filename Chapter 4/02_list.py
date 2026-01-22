friends = ["jignesh", "apple", "sailesh", 5, 345.06, False, "mukesh"]
print(friends)

friends.append("nayak")# append = add at the end
print(friends)

friends.insert(3, "harry") #insert works like .insert(position, object to insert)
# it iserts harry such that harry's index is 3
print(friends)

friends.pop(6)#deletes object indexed 6 form container
print(friends)
print(friends.pop(6))#prints value of whatever is indexed 6 in the list.

#list functions return a none value hence chaining functions can't be created
L = [1, 54, 65 ,78, 999,46, 89, 91]
L.sort()#arranges list of numners in ascending order
a = L.sort()#assign value of l.sort() to a
print(a)# proves that list functions return none
print(L)
L.reverse()#arranges list of numners in descending order
print(L)
L.remove(65)
L.remove(78)
print(L)
 
print(f"Original List: {L}")#prints original list
