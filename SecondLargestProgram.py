
numbers = [12, 45, 67, 45, 89, 23]


largest = second_largest = numbers[0]


for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num


print("The second largest number is:", second_largest)
