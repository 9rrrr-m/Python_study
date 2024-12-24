import sys
# A: 81~100, B: 61~80, C: 41~60, D: 21~40, E: 0~20
score = int(input("score: "))

if 81 < score <= 100:
    print("grade is A")
elif 61 < score <= 80:
    print("grade is B")
elif 41 < score <= 60:
    print("grade is C")
elif 21 < score <= 40:
    print("grade is D")
elif 0 <= score <= 20:
    print("grade is E")
else:
    print("[ FAIL ] 잘못된 점수 입력입니다.")
    sys.exit(1)
