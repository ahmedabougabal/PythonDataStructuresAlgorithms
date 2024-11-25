<!-- @format -->

## Basics

### Time and Space Complexity

- **Time Complexity**: Measures the time an algorithm takes relative to input size (Big O).
- **Space Complexity**: Measures memory usage relative to input size.

### Big O, Big Omega, Big Theta

- **Big O**: Upper bound (worst-case).
- **Big Omega**: Lower bound (best-case).
- **Big Theta**: Tight bound (when upper and lower are the same).

## Recursion

- **Base Case**: Stops recursion.
- **Recursive Case**: Calls itself with a smaller input.

## Pointers and Memory Management (C++ specific)

- **Pointers**: Variables storing memory addresses.
- **Dynamic Memory Allocation**: `new` and `delete` in C++.
- **Memory Leaks**: Forgetting to deallocate memory.

## Templates

- **Templates**: Generalize functions/classes to work with any data type (C++ feature).

---

## Data Structures

### Arrays

- **1D Arrays**: Store elements in a linear sequence.
- **Multi-dimensional Arrays**: Store elements in a grid.
- **Dynamic Arrays**:
  - **C++**: `std::vector`
  - **Python**: Lists are dynamic by default.

### Linked Lists

- **Singly Linked List**: Each node points to the next.
- **Doubly Linked List**: Nodes point both ways.

### Stacks and Queues

- **Stack**:
  - **C++**: Use `std::stack`.
  - **Python**: Use lists with `append()` and `pop()`.
- **Queue**:
  - **C++**: Use `std::queue`.
  - **Python**: Use `collections.deque`.

### Hashing

- **C++**: Use `std::unordered_map`.
- **Python**: Use `dict`.

### Trees

- **Binary Search Tree (BST)**: Efficient search and insertion, O(log n) average time.
- **AVL Tree**: Self-balancing BST.

### Graphs

- **Adjacency List**:
  - **C++**: `vector<vector<int>>`.
  - **Python**: `defaultdict(list)`.

---

## Algorithms

### Sorting Algorithms

- **Bubble Sort**: O(n²).
- **Quick Sort**: O(n log n) on average.

### Searching

- **Binary Search**: O(log n) for sorted data.
  - **C++**: `std::lower_bound`.
  - **Python**: `bisect.bisect_left`.

---

## Bit Manipulation

### XOR Operations

- **Useful for swapping variables**:
  - **C++**: `a ^= b; b ^= a; a ^= b;`
  - **Python**: `a ^= b; b ^= a; a ^= b`
- **Finding unique element in array**:
  - **C++**:
    ```cpp
    int findUnique(vector<int>& arr) {
        int res = 0;
        for (int num : arr) res ^= num;
        return res;
    }
    ```
  - **Python**:
    ```python
    def find_unique(arr):
        res = 0
        for num in arr:
            res ^= num
        return res
    ```

### Bit Masks

- **Set the k-th bit**:
  - **C++**: `mask = 1 << k;`
  - **Python**: `mask = 1 << k`

### Subset Generation

- **Iterating over all subsets**:
  - **C++**:
    ```cpp
    for (int mask = 0; mask < (1 << n); ++mask) {
        // process each subset
    }
    ```
  - **Python**:
    ```python
    for mask in range(1 << n):
        # process each subset
    ```

### Counting Set Bits

- **Brian Kernighan’s algorithm**:
  - **C++**:
    ```cpp
    int countSetBits(int n) {
        int count = 0;
        while (n) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
    ```
  - **Python**:
    ```python
    def count_set_bits(n):
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
    ```

---

## Miscellaneous Algorithms

### Two-pointer Technique

- **Efficient array traversal**:
  - **C++**:
    ```cpp
    while (left < right) {
        // process with two pointers
        left++; right--;
    }
    ```
  - **Python**:
    ```python
    while left < right:
        # process with two pointers
        left += 1
        right -= 1
    ```

### Sliding Window

- **Efficient window of elements**:
  - **C++**:
    ```cpp
    for (int i = 0; i < n; i++) {
        // process sliding window
    }
    ```
  - **Python**:
    ```python
    for i in range(n):
        # process sliding window
    ```

### Fast Exponentiation

- **Exponentiation by squaring**:
  - **C++**:
    ```cpp
    int power(int x, int y) {
        int res = 1;
        while (y > 0) {
            if (y % 2 == 1) res = res * x;
            y /= 2;
            x = x * x;
        }
        return res;
    }
    ```
  - **Python**:
    ```python
    def power(x, y):
        res = 1
        while y > 0:
            if y % 2 == 1:
                res *= x
            y //= 2
            x *= x
        return res
    ```

---

## Practice and Problem-Solving

### Online Judges

- **LeetCode, Codeforces, HackerRank** for coding problems and competitions.

### Debugging and Optimization

- **Tools**: Debuggers, print statements, unit tests.
- **Optimize**: Reduce time and space complexity.
