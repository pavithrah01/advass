def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
arr = [8, 3, 1, 5, 2, 7, 4, 6]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
