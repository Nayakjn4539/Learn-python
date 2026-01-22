name = "Jignesh is a  wondeful guy and he is very slefish "
print(name.find(" "))# counts and prints position of " "- single space - reported dat belongs to parent string
print(name.find("  "))
print(name.find("    "))#results in -1 as there is no triple space

print(name.replace("  ", " "))# replaces double spaces with a single space
a = name.replace("  ", " ").replace("slefish", "helpful")
print(a)