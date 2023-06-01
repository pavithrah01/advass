def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    Returns the index of the target element if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(array, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")


