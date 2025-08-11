def tuple_with_max_sum(tuples_list):
    if not tuples_list:
        return None 

    return max(tuples_list, key=sum)

tuples = [(1, 2), (3, 4), (5, 1)]
result = tuple_with_max_sum(tuples)
print("Tuple with maximum sum:", result)