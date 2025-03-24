import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

input_string = input("Nhập đữ liệu để hash bằng SHA-256: ")
sha256_hash = calculate_sha256_hash(input_string)
print("Giá trị hash SHA-256 là: ", sha256_hash)
