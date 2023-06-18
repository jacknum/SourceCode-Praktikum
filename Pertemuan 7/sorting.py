import timeit

print("Ascending")
print(" ")

#insertion short
def insertion_sort(array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    stop = timeit.default_timer()
    print(f"Insertion sort successful! elapsed time: + {stop - start}")
    return array

#bubble sorting
def bubble_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    stop =timeit.default_timer()
    print(f"Bubble sort successful! elapsed time: + {stop - start}")
    return array

#selection sort
def selection_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    
    stop =timeit.default_timer()
    print(f"Selection sort successful! elapsed time: + {stop - start}")
    return array

list_1 = [8,3,1,2,9,67,4,33]
list_2 = [9,4,5,10,14,3,23]
list_3 = [99,22,55,44,88,66]
print(f"Before: {list_1}")
print(f"After: {insertion_sort(list_1)}")
print(f"After: {bubble_sort(list_2)}")
print(f"After: {selection_sort(list_3)}")