alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Второй алфавит нужен на случай если будем шифровать поледние буквы алфавита => Z - C при ключе шифрования 3
encrypt = input("Введите слово для шифрования.")
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + 3
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print(encrypted)

alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
decrypt = input("Введите слово для декодирования.")
decrypted = ""
for letter in decrypt:
    position = alphabet.find(letter)
    newPosition = position - 3
    if letter in alphabet:
        decrypted = decrypted + alphabet[newPosition]
    else:
        decrypted = decrypted + letter
print(decrypted)