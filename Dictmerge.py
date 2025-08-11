def merge_dictionaries(dict1, dict2):
   
    merged = dict1.copy()  
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict_a = {'a': 10, 'b': 5, 'c': 3}
dict_b = {'b': 7, 'c': 2, 'd': 4}

result = merge_dictionaries(dict_a, dict_b)
print(result)
