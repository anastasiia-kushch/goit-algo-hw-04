'''
This Python script compares the execution times of three sorting algorithms: insertion sort, merge sort, and Python's built-in Timsort (via the sorted function). It measures their performance on both small and large datasets to empirically validate the theoretical time complexities of these algorithms.
'''

import random
import timeit


# Сортування вставками
def insertion_sort(lst):
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst



# Сортування злиттям
def merge_sort(arr):
    arr = arr[:]
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1


    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Замір часу
print("Small dataset:")
small_data = [5, 3, 8, 6, 2, 7, 4, 1]
print("Insertion sort:", timeit.timeit(lambda: insertion_sort(small_data), number=10))
print("Merge sort:", timeit.timeit(lambda: merge_sort(small_data), number=10))
print("Timsort (sorted):", timeit.timeit(lambda: sorted(small_data), number=10))

print("\nLarge dataset:")
large_data = [random.randint(1, 1000000) for _ in range (10000)]
print("Insertion sort:", timeit.timeit(lambda: insertion_sort(large_data), number=1))
print("Merge sort:", timeit.timeit(lambda: merge_sort(large_data), number=1))
print("Timsort (sorted):", timeit.timeit(lambda: sorted(large_data), number=1))