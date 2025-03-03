from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)
vigenere_cipher = VigenereCipher()
caesar_cipher = CaesarCipher()

#CAESAR CIPHER
@app.route('/api/caesar/encrypt', methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})
@app.route('/api/caesar/decrypt', methods=["POST"])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypted_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#VIGENERE CIPHER
@app.route('/api/vigenere/encrypt', methods=["POST"])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/vigenere/decrypt', methods=["POST"])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)