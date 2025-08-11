def count_element_in_tuple(tup, element):
  
    count = 0
    for item in tup:
        if item == element:
            count += 1
    return count
my_tuple = ('apple', 'banana', 'apple', 'cherry', 'apple')
element_to_count = 'apple'

result = count_element_in_tuple(my_tuple, element_to_count)
print(f"The element '{element_to_count}' appears {result} times.")
