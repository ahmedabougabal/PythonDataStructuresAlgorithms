"""
Insertion Sort Algorithm Implementation
"""


def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        position = i - 1
        while position >= 0 and current < array[position]:  # while loop shifts the elements in the sorted portion
            # (elements on the left of the current index) to the right to make room for the coming element (from the right side)'(unsorted portion)'
            array[position + 1] = array[position]
            position -= 1

        # then I have to insert current element i am on to the correct position
        array[position + 1] = current
    return array


arr = [12, 43, 65, 3, 65, 7, 45, 2, 3, 61, 0, 1]

print(f"sorted array : {insertionSort(arr)}")

# BEST CASE O(N) --> Array is sorted
# WORST CASE O(n^2) --> Array is reversed
