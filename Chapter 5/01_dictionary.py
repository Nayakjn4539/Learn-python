marks = {
    "harry": 98,
    "shubham": 97,
    "sailesh": 99, 
    "mukesh": 100,
    "jignesh": 96,
}

print(marks, type(marks))     
print(marks["harry"], type("harry"), marks["shubham"], type(["shubham"]))
#[] tell pythin to create a list with given one element "harry" and report type as list
#{} tell pythin to create a dictionary with given one key value pair harry:98 and report type as dictionary 
#() tell pythin to create a tupple with given one element 1 and report type of the tupple

print("Type of the value of 'harry':", type(marks["harry"])) 
#This correctly accesses the value associated with the key "harry" (which is the integer 98) and prints its type as <class 'int'>.

print(marks.get("harry"), type(marks.get("harry")))
# .get() method is used to access value associated with key in dictionary
