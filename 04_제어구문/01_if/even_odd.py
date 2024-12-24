num1 = int(input("input num1 : "))
num2 = int(input("input num2 : "))

if num1 >= num2:
    big_num = num1
else:
    big_num = num2

print(big_num)

if big_num % 2 == 1:
    print("odd number")
else:
    print("even number")
