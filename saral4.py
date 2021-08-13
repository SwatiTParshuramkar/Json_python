dict1 = {'4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
sorted_values = sorted(dict1.values()) # Sort the values(used when you need the function.)
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i :
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)