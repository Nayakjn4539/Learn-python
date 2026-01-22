s = {1, 34, 45, 65, 76, 87, 45, 5, "harry"}#wont return duplicate elements multiple times

print (s, type(s))

s.add(566)
print (s)

s.update([4, 6]) #Adds multiple elements (from a list, tuple, or another set)
print(s)

s.remove(76)#removes element from set, returns error if element not present
s.discard(76)#removes 76 and does nothing if not found
print (s)

s.pop()#removes adn returns a random element
print(s)

s.clear()#Removes all elements, leaving an empty set.
print(s)