def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Select a pivot element
    pivot = arr[len(arr) // 2]

    # Partition the array into two subarrays
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Recursively sort the subarrays
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
arr = [8, 3, 1, 5, 2, 7, 4, 6]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
