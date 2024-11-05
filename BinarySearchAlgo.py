"""
Implementation of Binary Search Algorithm
"""


def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == target:
            return f"Number {target} is found at index {mid}"
        else:
            if array[mid] < target:
                low = mid + 1
            if array[mid] > target:
                high = mid - 1
    return "Number not found"


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch(arr, 4))
