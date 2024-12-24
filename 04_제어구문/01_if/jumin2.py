# Main
jumin = input("주민등록번호: ").split('-')

jumin_num = jumin[0] + jumin[1]

# first test
testnum = '234567892345'
first_result = 0
for i in range(len(testnum)):
    first_result += (int(testnum[i]) * int(jumin_num[i]))

# second test
second_result = first_result % 11

# third test
third_result = 11 - second_result
if third_result == int(jumin_num[12]):
    print("유효한 주민번호 입니다.")
else:
    print("유효한 주민번호가 아닙니다.")
