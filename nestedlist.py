def update_nested_value(d, outer_key, inner_key, new_value):
    
    if outer_key in d and inner_key in d[outer_key]:
        d[outer_key][inner_key] = new_value
    else:
        print("Specified keys not found.")
    return d
data = {'user': {'name': 'Alice', 'age': 25}}

# Update age to 30
updated_data = update_nested_value(data, 'user', 'age', 30)

print(updated_data)
