# String-Encryption
# Code Explanation
This code implements the Caesar cipher, a simple encryption algorithm that shifts each letter in the plaintext by a specified number of positions in the alphabet. The code is written in Python, and it consists of two parts: the encrypt function and the main code.

The encrypt function takes two parameters: plaintext and shift.

    1.ciphertext = "" creates an empty string that will be used to store the encrypted message.

    2.The for loop for char in plaintext: loops through each character in the plaintext string.

    3.if char.isalpha(): checks if the current character is a letter. If it is, the letter is encrypted, otherwise, it is left unchanged.

    4.shift_char = chr((ord(char) - 65 + shift) % 26 + 65) calculates the encrypted letter. ord(char) returns the Unicode code point of the character, - 65 makes 'A' equal to 0, + shift shifts the letter by the specified number of positions, and % 26 wraps around the alphabet so that 'Z' + 1 becomes 'A'. chr((... + 65) converts the number back into a character.

    5.ciphertext += shift_char adds the encrypted letter to the ciphertext string.

    6.else: ciphertext += char adds the unencrypted character to the ciphertext string if the character is not a letter.

The main code starts with plaintext = input("Enter plaintext: "), which prompts the user to enter the message to be encrypted.

shift = int(input("Enter shift: ")) prompts the user to enter the shift value, which is converted to an integer.

ciphertext = encrypt(plaintext, shift) calls the encrypt function and stores the returned encrypted message in the ciphertext variable.

print("Plaintext:", plaintext) and print("Ciphertext:", ciphertext) print the original message and the encrypted message, respectively.

To execute the code, save it to a file with a .py extension and run it using a Python interpreter. You can do this from the command line by navigating to the directory where the file is saved and entering python filename.py.

# Example Of Code Execution

Here's an example of what running the code might look like:
Enter plaintext: Hello World
Enter shift: 3
Plaintext: Hello World
Ciphertext: Khoor Zruog

In this example, the user entered the plaintext Hello World and a shift value of 3. The encrypted message Khoor Zruog was generated and displayed as the output.

