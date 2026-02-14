my_set = {"Apple", "Banana", "Cherry"}

for fruit in my_set:
    print(fruit)

# Output might be:
# Banana
# Apple
# Cherry
# (The order is not guaranteed!)

#If you just write for x in my_dict:, Python assumes you want the Keys
scores = {"Alice": 90, "Bob": 80}

for name in scores:
    print(name)
    
# Output:
# Alice
# Bob