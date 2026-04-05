# python program to convert celcius to farenheit

'''
formula is 9C = 5F - 160
'''

def ctof(C):
    return(9/5 * C + 32)

C = float(input("Enter the temperature in Celscius: "))
print(f"The {C} degree celcius in Farenheit is {ctof(C)}")

#Another Method
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter Temperature in f: "))
c = f_to_c(f)
print(f"{round(c, 2)}C")