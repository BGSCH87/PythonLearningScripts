from random import randint

text = input("Enter the message you would like to encipher: ")
text = text.upper()
shift = randint(1, 25)


def caesar_cipher_up(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            decoded_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            decoded_text += char

    print(f"Decoded Message: {decoded_text}")


def ceasar_cipher_down(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            decoded_text += chr((ord(char) - 65 + (26 + shift)) % 26 + 65)
        else:
            decoded_text += char

    print(f"Decoded Message: {decoded_text}")


print(
    f"Your original message is {text}. We will now use a random to int to Decipher the message"
)
caesar_cipher_up(text, shift)
print(f"Enigma value: {shift} \nWe will use this value to decipher the message")
ceasar_cipher_down(text, shift)
