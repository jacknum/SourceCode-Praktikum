def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"keyword {keyword} has found at index {i}")
            return i
    print(f"keyword {keyword}not found")
    return -1

data = [23, 3, 4, 78, 9, 32]
keyword = input("input keyword: ")
linear_search(keyword, data)