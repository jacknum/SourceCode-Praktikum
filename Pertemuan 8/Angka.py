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
            print(f"Angka {bil} ditemukan pada index {mid}")
            return mid
    print(f"Angka {bil} tidak ditemukan")
    return -1

data = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]
bil = input("Masukkan Angka: ")
binary_search(bil, data)



