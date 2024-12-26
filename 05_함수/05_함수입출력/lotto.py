import random


def lotto_number(max_choice):
    lotto_numbers = []
    i = 1
    while i <= max_choice:
        num = random.randint(1, 45)
        if num not in lotto_numbers:
            lotto_numbers.append(num)
            i += 1
    lotto_numbers.sort()
    print(lotto_numbers)


lotto_number(6)
