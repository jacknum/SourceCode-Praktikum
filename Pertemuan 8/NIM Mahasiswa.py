def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def binary_search(keyword, data):
    sorted_data = bubble_sort(data)
    print(f"Data (sorted) = {sorted_data}")
    left = 0
    right = len(sorted_data) - 1
    while left <= right:
        mid = (left + right)//2
        str_data = str(sorted_data[mid]).lower()
        if str_data > keyword.lower():
            right = mid - 1
        elif str_data < keyword.lower():
            left = mid + 1
        else:
            print(f"Mahasiswa dengan NIM {keyword} ditemukan pada index {mid}")
            return mid
    print(f"Mahasiswa dengan NIM {NIM} tidak ditemukan")
    return -1

data = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 20103011, 20103003, 20103009, 20103021, 20103006, 20103015, 20103013, 20103007]
NIM = input("Masukkan NIM: ")
binary_search(NIM, data)


