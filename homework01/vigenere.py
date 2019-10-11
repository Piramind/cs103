def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ''
    text_len = len(plaintext)
    key_len = len(keyword)
    new_key = list()
    for i in range(text_len):
        new_key.append(keyword[i % key_len])
    shifts = list()
    for char in new_key:
        code = ord(char)
        if 97 <= code <= 122:
            shifts.append(code - 97)
        elif 65 <= code <= 90:
            shifts.append(code - 65)
    for index, char in enumerate(plaintext):
        code = ord(char)
        if 97 <= code <= 122:
            code += shifts[index]
            if not 97 <= code <= 122:
                code -= 26
        elif 65 <= code <= 90:
            code += shifts[index]
            if not 65 <= code <= 90:
                code -= 26
        ciphertext += chr(code)
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ''
    text_len = len(ciphertext)
    key_len = len(keyword)
    new_key = list()
    for i in range(text_len):
        new_key.append(keyword[i % key_len])
    shifts = list()
    for char in new_key:
        code = ord(char)
        if 97 <= code <= 122:
            shifts.append(code - 97)
        elif 65 <= code <= 90:
            shifts.append(code - 65)
    for index, char in enumerate(ciphertext):
        code = ord(char)
        if 97 <= code <= 122:
            code -= shifts[index]
            if not 97 <= code <= 122:
                code += 26
        elif 65 <= code <= 90:
            code -= shifts[index]
            if not 65 <= code <= 90:
                code += 26
        plaintext += chr(code)
    return plaintext