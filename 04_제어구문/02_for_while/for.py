# string
str1 = 'Hello World'

for i in str1:
    print(i)

# list
list1 = ['a', 'b', 'c', [1, 2, 3]]

for i in list1:
    print(i)

# tuple
tuple1 = ('a', 'b', 'c', [1, 2, 3])

for i in tuple1:
    print(i)

# dict
dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

for k, v in dict1.items():
    print(k, v)

# set
set1 = {'a', 'b', 'c'}

for i in set1:
    print(i)

# example
a = [(1, 2), (3, 4), (5, 6)]

for (first, last) in a:
    print(first + last)
