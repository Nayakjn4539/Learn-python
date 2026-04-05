'''
Write a python function to remove a given word from a list and strip it at the same time
'''

def rem_fr_lst(list_data, word):
    new_list = []
    for item in list_data:
        stripped = item.strip()
        if stripped != word:
            new_list.append(stripped)
    return new_list

print(rem_fr_lst(["apple", "banana", "cherry", "date"], "banana"))
            
    