def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số, cách nhau = dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_turple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ list: ", my_turple)
