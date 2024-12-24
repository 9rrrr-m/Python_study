# A + 5 = F
encbook = {'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L',
           'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S',
           'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z',
           'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'}

# decbook
decbook = {}
for k in encbook:
    decbook[encbook[k]] = k

print("decbook:", decbook)

# encryption
plaintext = 'HeLlO woRLD123'
print("plaintext  :", plaintext)

ciphertext = ''
for i in plaintext.upper():
    if i in encbook:
        ciphertext += encbook[i]
    else:
        ciphertext += i

print("ciphertext :", ciphertext)

# decryption
decrypttext = ''
for i in ciphertext:
    if i in encbook:
        decrypttext += decbook[i]
    else:
        decrypttext += i

print("decrypttext:", decrypttext)
