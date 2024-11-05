"""
Selection sort Algorithm
traverses the array and finds the smallest element in the array, and then swaps it with the
current element
Time Complexity: O(n^2)
"""


def selectionSort(array):
    n = len(array)
    for i in range(0, n):
        smallest = i
        for j in range(i + 1, n):
            if array[j] < array[smallest]:
                smallest = j  # [Bug Solved] Update the index here not the value
        temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp
    return array


arr = [23, 43, 65, 2, 3, 54, 100, 1]
print(f"Original : {arr}")
print(f"Sorted using implemented function : {selectionSort(arr)}")
print(f"Sorted reference : {sorted(arr)}")
