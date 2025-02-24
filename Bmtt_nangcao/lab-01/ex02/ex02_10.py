def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_str = input("Nhập chuỗi cần đảo ngược: ")
print(f"Chuỗi sau khi đảo ngược: {dao_nguoc_chuoi(input_str)}")