def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
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
     """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for char in ciphertext:
        code = ord(char)
        if 97 <= code <= 122 or 65 <= code <= 90:
            code -= 3
            if not (97 <= code <= 122 or 65 <= code <= 90):
                code += 26
        plaintext += chr(code)
    return plaintext
