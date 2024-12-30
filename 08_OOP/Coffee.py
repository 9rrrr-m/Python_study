class Coffee:
    def __init__(self):
        self.total_amount = 10
        self.total_amount_price = 5000
        self.coffee_price = 300
        self.isTrue = True

    def get(self, req_coffee_nums):
        self.total_amount -= req_coffee_nums
        self.total_amount_price -= self.return_price
        print(f"커피가 {req_coffee_nums}잔 나왔습니다.")
        print(f"거스름돈 {self.return_price}원을 반환합니다.")
        self.info()
        if self.total_amount == 0 or self.total_amount_price == 0:
            print("=========================================")
            print("커피를 제공할 수 없습니다. 프로그램을 종료합니다.")
            self.isTrue = False

    def check_amount(self):
        if (self.total_amount - self.req_coffee_nums >= 0
                and self.total_amount_price >= self.return_price):
            return True
        else:
            return False

    def info(self):
        print("-----------------------------------------")
        print(f"현재 남은 커피는 {self.total_amount}개 입니다.")
        print(f"현재 남은 총 금액은 {self.total_amount_price}원 입니다.")

    def request(self):
        while self.isTrue:
            print("=========================================")
            self.put_price = int(input("금액을 넣어주세요.: "))
            if self.put_price < 300:
                print("금액이 부족합니다. 다시 입력해주세요.")
                continue
            self.req_coffee_nums = int(input("주문 수량을 입력하세요.: "))
            if self.req_coffee_nums <= 0:
                print("수량은 1개 이상이어야 합니다. 다시 입력해주세요.")
                continue
            print("=========================================")
            self.return_price = self.put_price - (self.req_coffee_nums * 300)
            if self.check_amount():
                self.get(self.req_coffee_nums)
            else:
                print("커피를 제공할 수 없습니다. 금액을 반환합니다.")
                self.info()
                continue


coffee_machine = Coffee()
coffee_machine.request()
