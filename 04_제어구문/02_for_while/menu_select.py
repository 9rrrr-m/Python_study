# Functions
def add():
    num1 = int(input("1번째 숫자를 입력하세요.: "))
    num2 = int(input("1번째 숫자를 입력하세요.: "))
    print(num1 + num2)


def delete():
    print("DEL")


def show_list():
    print("LIST")


# Main
prompt = """
1. add
2. del
3. list
4. quit
"""

number = 0
while number != 4:
    print(prompt)
    number = int(input("Enter number: "))
    if number == 1:
        add()
    elif number == 2:
        delete()
    elif number == 3:
        show_list()
    else:
        print("올바른 번호를 입력하세요.")
