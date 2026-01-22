marks = {
    "harry": 98,
    "shubham": 97,
    "sailesh": 99, 
    "mukesh": 100,
    "jignesh": 96,
    0: "mukesh",
}
print(marks.items()) #.items() returns a dict_items view object containing key–value tuples
print(type(marks.items())) #type of .items() is dict_items which is a special type in python

print("the keys in dectionary are: ", marks.keys()) 
#.keys() returns a dict_keys view object, not a list

print("the values of marks are: ",marks.values()) 
#.values() returns a dict_values view object, not a list 

marks.update({"harry":99}) 
#can even add non existing data to the original dictionary
#updates the mutable dictionary for all codes that run after this line of code.
print("the updated marks are: ",marks)

# get function accepts two arguments key and default value; ().get("key", "default value"))
#default value is optional amd if not provided it is considered as None
#default value is returned only when key is not present in dictionary
print(marks.get("harry")) #prints marks corresponding to harry
print(marks.get("shivika")) #print None as key "shivika" is not present in dictionary
print(marks.get("harry", "shivika")) 
#prints 99 as harry is present in dictionary
#since harry has a value the "shivika" is ignored
print(marks.get("mukesh", "harry"))
#since mukesh has a value the "harry" is ignored
print(marks.get("shivika", "not found"))
#here shivika is not present in dictionary hence "not found" is printed
#if "not found" was replaced with any other string that string would have been printed 
print(marks.get("shivika", "shivika"))
#here first shivika is not present in dictionary, look for second word which is shivika hence "shivika" is printed

print(len(marks))#prints length of dictionary