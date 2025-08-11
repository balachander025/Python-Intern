def sort_dict_by_value_desc(d):
 
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

my_dict = {'apple': 3, 'banana': 5, 'orange': 2, 'kiwi': 7}

sorted_result = sort_dict_by_value_desc(my_dict)
print(sorted_result)

