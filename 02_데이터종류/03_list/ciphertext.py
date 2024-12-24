plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

plaintext_size = len(plaintext)
ciphertext_list = []

for i in range(plaintext_size):
    if i <= 2:
        ciphertext_list.append(plaintext[i])

ciphertext = plaintext[3:] + ''.join(ciphertext_list)
print(ciphertext)

# 모듈러 연산 사용
ciphertext = ''
for i, ch in enumerate(plaintext):
    # print(i)
    ciphertext += plaintext[(i + 3) % len(plaintext)]

print(ciphertext)
