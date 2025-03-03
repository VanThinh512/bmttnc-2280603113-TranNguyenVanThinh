class VigenereCipher:
    def __init__(self):
        pass
    def vigenere_encrypt(self, plaintext, key):
        encrypted_text = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                key_shift = ord(key[key_index %len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) + key_shift - ord('A')) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) + key_shift - ord('a')) % 26 + ord('a'))
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index %len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - key_shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - key_shift - ord('a')) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
    