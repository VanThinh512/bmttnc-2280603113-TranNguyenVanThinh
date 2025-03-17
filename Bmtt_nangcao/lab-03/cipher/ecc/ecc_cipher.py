import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()  # Tạo khóa riêng
        vk = sk.get_verifying_key()       # Sửa lại method name

        with open('cipher/ecc/keys/private_key.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('cipher/ecc/keys/public_key.pem', 'wb') as p:
            p.write(vk.to_pem())

        return sk, vk

    def load_keys(self):
        with open('cipher/ecc/keys/private_key.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('cipher/ecc/keys/public_key.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            # Sửa lại thứ tự tham số và xử lý encoding
            return vk.verify(bytes.fromhex(signature), message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False