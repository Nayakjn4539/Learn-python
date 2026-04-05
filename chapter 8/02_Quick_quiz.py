def goodDay():
    name = input("enter your name here: ")
    return f"Good Day, {name}" # Combines them into one string

a = goodDay()
print(f"{a}")


# another way to do this

def wellday():
    name = input("Enter your name: ")
    ending = input("how do you wish to be greeted? ")
    print(f"{name}, {ending}")
    #print(ending)

wellday()
wellday()