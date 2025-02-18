# program that is creating a list of random numbers and then feeding list to 2 sorting algorithms
# once fed into the sorting algorithms, using timeit to test to see how long it takes both algorithms
import random
import timeit

# creating large dataset of random numbers, stored in a list
large_random_list = []
n = 10000
for i in range(n):
    large_random_list.append(random.randint(1,10000))

# the 2 sorting algorithms being used are bubble sort and merge sort
# Bubble sort is first

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Measuring the time taken by bubble sort on the list
bubble_sort_time = timeit.timeit(lambda: bubble_sort(large_random_list.copy()), number=1)

print("Original dataset:", large_random_list[:10], "...")
print("Sorting using Bubble Sort...")
print("Sorted dataset:", large_random_list[:10], "...")
print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")
print()
print()
# 2nd sorting algorithm is Merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Measuring the time taken by merge sort
merge_sort_time = timeit.timeit(lambda: merge_sort(large_random_list.copy()), number=1)

print("Original dataset:", large_random_list[:10], "...")
print("Sorting using Merge Sort...")
print("Sorted dataset:", merge_sort(large_random_list.copy())[:10], "...")
print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
print()
print()
print(f"Bubble sort time: {bubble_sort_time:.6f} seconds and Merge sort time: {merge_sort_time:.6f} seconds ")