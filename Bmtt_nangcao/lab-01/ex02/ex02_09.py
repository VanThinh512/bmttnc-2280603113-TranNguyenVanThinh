def kiem_tra_so_nguyen_to(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
num = int(input("Nhập số nguyên dương: "))
if kiem_tra_so_nguyen_to(num):
    print(f"{num} là số nguyên tố")
else:
    print(f"{num} không phải là số nguyên tố")