coffee = 5
while True:
    if not coffee:
        print("남은 커피가 없습니다. 판매를 중지합니다.")
        break

    money = int(input("돈을 넣어주세요.: "))
    if money > 300:
        print("커피가 나왔습니다.")
        print("거스름돈을 반환합니다.: %d" % (money - 300))
        coffee -= 1
    elif money == 300:
        print("커피가 나왔습니다.")
        coffee -= 1
    else:
        print("잔액이 부족합니다. 금액을 반환합니다.: %d" % money)

    print("남은 커피의 개수는 %d개 입니다." % coffee)
    print()
