from random import randint


def caesar_cipher_up(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            encoded_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encoded_text += char

    print(f"Encoded Message: {encoded_text}")
    return encoded_text


def caesar_cipher_down(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            decoded_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decoded_text += char

    print(f"Decoded Message: {decoded_text}")
    return decoded_text


if __name__ == "__main__":
    text = input("Enter the message you would like to encipher: ")
    text = text.upper()
    shift = randint(1, 25)

    print(
        f"Your original message is {text}. We will now use a random int (KEY) to decipher the message"
    )
    encoded = caesar_cipher_up(text, shift)
    print(
        f"Enigma value: {shift} \nWe will use this KEY ({shift}) to decipher the message"
    )
    caesar_cipher_down(encoded, shift)
