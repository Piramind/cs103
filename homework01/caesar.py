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


