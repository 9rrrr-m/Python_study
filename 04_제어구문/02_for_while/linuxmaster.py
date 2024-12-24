marks = [90, 25, 67, 45, 80]

for i in range(len(marks)):
    if marks[i] >= 60:
        print("%d 번 학생: 합격" % (i + 1))
    else:
        print("%d 번 학생: 불합격" % (i + 1))
