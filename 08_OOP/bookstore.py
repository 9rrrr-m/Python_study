class Book:
    def __init__(self, title, price, author):
        print("책 객체를 새로 생성하였습니다.")
        self.setData(title, price, author)

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목 :', self.title)
        print('가격 :', self.price)
        print('저자 :', self.author)


book = Book("해리포터", 7000, "조앤K롤링")
book.printData()
