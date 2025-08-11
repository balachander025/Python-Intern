def frequency_count(lst):
    
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
result = frequency_count(my_list)
print(result)
