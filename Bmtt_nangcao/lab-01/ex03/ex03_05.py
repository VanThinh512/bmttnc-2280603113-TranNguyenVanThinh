def dem_so_lan_xuat_hien(lst):
    count_dist = {}
    for i in lst:
        if i in count_dist:
            count_dist[i] += 1
        else:
            count_dist[i] = 1
    return count_dist
input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)