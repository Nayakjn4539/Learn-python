'''
Write a python function to convert cms to inches
'''

def cms_to_inches(cms):
    return cms / 2.54

cms = float(input("Enter the value in cms: "))
print(f"The value in inches is {round(cms_to_inches(cms), 2)}")