import os

if os.path.exists('t.txt'):
    os.remove('t.txt')
    print('The file removed.')
else:
    print('The file does not exist.')