num = int(input("구구단: "))

for i in range(1, 10):
    print("%d x %d = %d" % (num, i, num * i))

for j in range(1, 10):
    if (num * j) % 2 == 1:
        print("%d x %d = %d" % (num, j, num * j))