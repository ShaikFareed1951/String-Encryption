def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext
plaintext = input("Enter plaintext: ")
shift = int(input("Enter shift: "))
ciphertext = encrypt(plaintext, shift)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
