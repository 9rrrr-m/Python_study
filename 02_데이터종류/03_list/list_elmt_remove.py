# 문제1
from os import remove

numbers = [1, 2, 3, 4, 5]

del numbers[3:]
print(numbers)

# 문제2
numbers = [1, 2, 3, 4, 5, 3, 2, 9, 10, 3]

# output: [1, 2, 4, 5, 3, 2, 9, 10, 3]
numbers.remove(3)
print(numbers)

# output: [1, 2, 4, 5, 2, 9, 10]
for i in numbers:
    if i == 3:
        numbers.remove(3)
print(numbers)

# print([for num in numbers if num != 3])
