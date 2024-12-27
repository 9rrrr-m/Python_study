import os

if not os.path.isdir('./test'):
    os.mkdir('./test')

content = """
반갑습니다. 
python 개발자 여러분 한살 더 드셨죠!
올 한해는... 행복한 가득한 한해가 되었으면 합니다.
"""

with open('./test/test.txt', 'w') as f:
    f.write(content)

with open('./test/test.txt') as f:
    print(f.read())

if os.path.isfile('./test/test.txt'):
    os.remove('./test/test.txt')
    print("파일이 정상적으로 삭제되었습니다.")
