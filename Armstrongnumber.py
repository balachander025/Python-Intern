
num = int(input("Enter a  number: "))


hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

armstrong_sum = (hundreds ** 3) + (tens ** 3) + (ones ** 3)


if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    