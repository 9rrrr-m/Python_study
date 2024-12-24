import time

for i in range(1, 11):
    print("나무를 %d번 찍었습니다." % i)
    time.sleep(1)
    if i == 10:
        print("나무가 넘어갔습니다.")
