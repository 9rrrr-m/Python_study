file_lists = ['hello.py', 'ex01.py', 'ex02.py', 'ch02.py', 'intro.hwp']

result = []
for i in file_lists:
    result.append(''.join(i.split('.')[:-1]))

print(result)
