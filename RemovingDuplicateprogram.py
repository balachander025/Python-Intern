numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates (order preserved):", unique_numbers)
