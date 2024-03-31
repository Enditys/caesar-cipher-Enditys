#Cipher code, allowed value to be set by user as well and not just a flat 5
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Get input from the user
sentence = input("Enter a sentence: ")
shift = int(input("Enter the shift value: "))

encrypted_sentence = caesar_cipher(sentence, shift)
print("The encrypted sentence is:", encrypted_sentence)