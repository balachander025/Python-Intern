def invert_dictionary(d):
    
    return {value: key for key, value in d.items()}

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted = invert_dictionary(original_dict)
print(inverted)

