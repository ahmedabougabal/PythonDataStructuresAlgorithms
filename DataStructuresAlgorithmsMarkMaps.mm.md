<!-- @format -->

# Basics

## Time and Space Complexity

- Time Complexity: Measures the amount of time an algorithm takes to run, relative to the input size. It is usually expressed using Big O notation.
- Space Complexity: Measures the amount of memory an algorithm uses relative to the input size.

## Big O, Big Omega, Big Theta

- Big O: Upper bound of the running time (worst-case scenario).
- Big Omega: Lower bound of the running time (best-case scenario).
- Big Theta: Tight bound, when the upper and lower bounds are the same.

## Recursion

- Recursion: A function that calls itself to solve a smaller instance of the same problem.
- Base Case: The condition that stops the recursion, preventing infinite loops.
- Recursive Case: The part of the function that calls itself with a smaller input.

## Pointers and Memory Management

- Pointers: Variables that store memory addresses.
- Dynamic Memory Allocation: Using `new` and `delete` in C++ to allocate and deallocate memory at runtime.
- Memory Leaks: Occur when memory is allocated but not deallocated, leading to memory inefficiency.

## Templates (Generic Programming)

- Templates: Allow functions and classes to operate with generic types.
- Type Flexibility: Enables code reusability across different data types without modification.

# Data Structures

## Arrays

### One-dimensional Arrays

- Store elements in a linear sequence.

### Multi-dimensional Arrays

- Store elements in a grid-like structure (e.g., 2D arrays).

### Dynamic Arrays (`std::vector`)

- Resizable arrays that automatically manage their own memory.

## Linked Lists

### Singly Linked List

- Each node points to the next node.

### Doubly Linked List

- Each node points to both the previous and next nodes.

### Circular Linked List

- The last node points back to the first node, forming a loop.

## Stacks

### Array Implementation

- Use a fixed-size array with a top pointer.

### Linked List Implementation

- Use a linked list with operations at the head.

### Applications

- Expression evaluation, function calls, undo mechanisms.

## Queues

### Simple Queue

- FIFO (First-In-First-Out) data structure.

### Circular Queue

- Optimizes space by wrapping around the array.

### Priority Queue

- Elements are dequeued in order of priority.

### Deque

- Allows insertion and deletion from both ends.

## Hashing

### Hash Tables

- Use a hash function to map keys to indices in an array.

### Collision Handling

- Techniques like chaining (linked lists) and open addressing (linear probing).

### `std::unordered_map`

- C++ standard library hash table implementation.

## Trees

### Binary Tree

- Each node has up to two children.

### Binary Search Tree (BST)

- Left child < Parent < Right child.

### AVL Tree

- Self-balancing BST with a balance factor.

### Red-Black Tree

- Self-balancing BST with coloring properties.

### Segment Tree

- Efficient for range queries and updates.

## Heaps

### Min-Heap

- Parent is less than or equal to children.

### Max-Heap

- Parent is greater than or equal to children.

### `std::priority_queue`

- C++ standard library heap implementation.

## Graphs

### Adjacency Matrix

- A 2D array representing graph connections.

### Adjacency List

- A list of lists representing graph connections.

### Directed Graphs

- Edges have a direction.

### Undirected Graphs

- Edges have no direction.

### Weighted Graphs

- Edges have associated weights.

### Disjoint Set Union (DSU)

- Union-Find data structure for managing disjoint sets.

## Strings

### Character Arrays

- Arrays of characters terminated by a null character.

### `std::string`

- C++ standard string class with dynamic resizing.

### Pattern Matching

- Algorithms like KMP and Rabin-Karp for efficient string searching.

# Algorithms

## Sorting

### Bubble Sort

- Repeatedly swaps adjacent elements if they are in the wrong order. O(n²) time.

### Selection Sort

- Selects the smallest element and places it at the beginning. O(n²) time.

### Insertion Sort

- Builds the final sorted array one item at a time. O(n²) time.

### Merge Sort

- Divides the array into halves, sorts them, and merges them. O(n log n) time.

### Quick Sort

- Chooses a pivot and partitions the array around it. O(n log n) average time.

### Heap Sort

- Uses a heap to repeatedly extract the maximum element. O(n log n) time.

### Counting Sort

- Non-comparison based sort, efficient for limited range of integers. O(n + k) time, where k is the range.

## Searching

### Linear Search

- Checks each element one by one. O(n) time.

### Binary Search

- Divides the search interval in half. O(log n) time for sorted data.

### Ternary Search

- Divides the search interval into thirds. O(log n) time for sorted data.

## Divide and Conquer

### Merge Sort

- Divides the array into halves, sorts them, and merges them.

### Quick Sort

- Partitions the array around a pivot and sorts the partitions.

### Binary Search

- Divides the search space in half at each step.

## Dynamic Programming (DP)

### Memoization

- Stores the results of expensive function calls and returns the cached result when the same inputs occur again.

### Tabulation

- Solves the problem iteratively, filling a table (array) from the bottom up.

### Knapsack Problem

- Select items to maximize value without exceeding capacity.

### Longest Common Subsequence (LCS)

- Finds the longest subsequence common to all sequences.

## Greedy Algorithms

### Activity Selection

- Selects the maximum number of non-overlapping activities.

### Huffman Encoding

- Builds an optimal prefix code for compressing data.

### Minimum Spanning Tree (MST)

- Kruskal's and Prim's algorithms find the MST of a graph.

## Backtracking

### N-Queens Problem

- Places N queens on an N×N board without attacking each other.

### Sudoku Solver

- Fills the grid following the Sudoku rules.

### Hamiltonian Cycle

- Finds a cycle that visits each vertex exactly once.

## Graph Algorithms

### BFS (Breadth-First Search)

- Traverses the graph level by level.

### DFS (Depth-First Search)

- Traverses the graph as far as possible along each branch.

### Dijkstra's Algorithm

- Finds the shortest path from a source to all other vertices in a graph with non-negative weights.

### Floyd-Warshall Algorithm

- Computes the shortest paths between all pairs of vertices.

### Bellman-Ford Algorithm

- Finds the shortest path from a source to all other vertices, handling negative weights.

### Kruskal's Algorithm

- Finds the MST using a greedy approach with Union-Find.

### Prim's Algorithm

- Finds the MST using a greedy approach with a priority queue.

## Bit Manipulation

### XOR Operations

- Useful for swapping variables and checking parity.

### Bit Masks

- Use bits to represent flags or sets.

### Subset Generation

- Use bits to represent subsets of a set.

### Counting Set Bits

- Counts the number of 1s in the binary representation of a number.

## Miscellaneous

### Two-pointer Technique

- Uses two pointers to traverse arrays or lists efficiently.

### Sliding Window

- Maintains a window of elements for efficient computation.

### Fast Exponentiation

- Computes powers efficiently using exponentiation by squaring.

### Topological Sorting

- Orders vertices in a DAG (Directed Acyclic Graph) such that for every directed edge uv, u comes before v.

### Trie (Prefix Tree)

- Efficient for storing and searching strings with common prefixes.

# Practice and Problem-Solving

## Online Judges (LeetCode, Codeforces, etc.)

- Platforms where you can practice coding problems and participate in contests.

## Competitive Programming

- Participate in programming contests to improve problem-solving skills.

## Coding Patterns

- Learn common coding patterns and techniques used in solving problems.

## Interview Prep

- Focus on mastering algorithms, data structures, and problem-solving techniques for interviews.

## Debugging and Optimization

- Use tools like debuggers, print statements, and unit tests to find and fix errors.
- Improve algorithm efficiency by reducing time and space complexity.
