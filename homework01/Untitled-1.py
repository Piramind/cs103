def encrypt_caesar(plaintext: str) -> str:
    ciphertext = ''
    for char in plaintext:
        key = ord(char)
        if 97 <= key <= 122 or 65 <= key <= 90:
            key += 3
            if not (97 <= key <= 122 or 65 <= key <= 90):
                key -= 26
        ciphertext += chr(key)
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    plaintext = ''
    for char in ciphertext:
        key = ord(char)
        if 97 <= key <= 122 or 65 <= key <= 90:
            code -= 3
            if not (97 <= key <= 122 or 65 <= key <= 90):
                code += 26
        plaintext += chr(key)
    return plaintext