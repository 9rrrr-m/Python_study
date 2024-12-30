class Fridge:
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print('냉장고 문이 열렸습니다.')

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f"냉장고 속에 {thing} 음식이 들어갔습니다.")
        else:
            print('음식을 냉장고에 넣으려면 문을 열어주세요.')

    def close(self):
        self.isOpened = False
        print('냉장고 문을 닫았습니다.')


class Food:
    pass
