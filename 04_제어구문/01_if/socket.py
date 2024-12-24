import socket

ip = '192.168.10.60'  # 문자열
port = 21  # 숫자

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.10.60", 21))
ans = s.recv(1024)
print(ans)

if 'vsFTPd 2.3.4' in str(ans):
    print('[  OK  ] Backdoor Command Execution')
elif 'vsFTPd 3.0.3' in str(ans):
    print('[  OK  ] Remote Denial of Service')
elif 'vsFTPd 2.0.5' in str(ans):
    print('deny_file Option Remote Denial of Service')
else:
    print('[ FAIL ] Not Vulnerable')
