<!-- @format -->

# PythonDataStructuresAlgorithms

**_I will document some of my DataStructures taken notes here, Stay Tuned..._**

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Project Status](https://img.shields.io/badge/status-Still%20in%20Progress-yellow)](https://github.com/yourusername/mernStackMilestoneProject_ITI)

<!-- ![Binary Tree](https://img.shields.io/badge/Data%20Structure-Binary%20Tree-blue)
![Linked List](https://img.shields.io/badge/Data%20Structure-Linked%20List-brightgreen) -->

![Profile Views](https://komarev.com/ghpvc/?username=ahmedabougabal&color=brightgreen)

# checkout the DSA MindMaps i just added :)

**_Mind map 1_**
![image](https://github.com/user-attachments/assets/b7297d5c-543b-42d7-8cb6-27ea21777e52)

**_Mind map 2_**
![image](https://github.com/user-attachments/assets/914f4463-0475-4b0d-bada-890ee8a81edc)

# Trees

- trees are used to store information.
- tree is usually upside down.
- each circle is called a node or a vertex.
- link between 2 nodes is an edge.

![image](https://github.com/user-attachments/assets/52695b9b-7247-4b18-a50b-0f12cf44c5b0)

- from the above tree, we deduce the following. . .
- the edge is the distance (connection) between 2 nodes, node 5 has no edge with node 4
- [Tree with n nodes has n - 1 edges](https://www.cs.purdue.edu/homes/spa/courses/sa12/mod8.pdf)
- the tree has 4 levels, levels (0,1,2,3)
- Node(1) has 2 children: 2 and 3
- The parent of Node(7) is node(2)
- Nodes {5, 9} are siblings (brothers)
- height (specific to each node) represents the number of edges on the longest downward path between a node(vertex) and a leaf.
- Tree of N levels has N-1 heights, since that the tree above has 4 levels, then the height is 4-1 = 3 edges
- the height of the node 1 (root) is 3 (start from the root to the longest path downward to the farest leaf)
- node 7 has a height = 0
- Node's Depth : the number of edges from the node to the root node.
  **_Difference between Depth and Height_**
  - depth is specific about 2 nodes (root node and the current node only)
  - height is going down from the node to the leaves. (height is about my current node and any other node (leaf) i can reach - longest path)
- there is only 1 path between any 2 nodes. (you are now at the root node and you wanted to go to the node 4, then there is only 1 way (simple tree)
- in a tree where every node has only 1 single parent, then there is only 1 path from a node to another.

**Sub Trees**

- recursive nature where each tree has a subtree and each subtree has another subtree.
- Problem solving tip: we deduce that when we want to get the elements of a tree, we will do this recursively.

# Binary Trees

- a tree where each node at least has at most 2 children (left and right nodes).
- a leaf node is a node with no children.

**this is a simple tree (a node has many children)**
![image](https://github.com/user-attachments/assets/896209b1-7bba-4d07-bdcd-c1a92d3d5433)

**this is a binary tree (each node has at most 2 children)**
![image](https://github.com/user-attachments/assets/61f26fc1-cb60-4e11-9841-9947f31100fe)

-- A linked List is a special case of a binary tree.

---
# binary tree traversal 1

traversal is a way of walking through an elements of a data structure.

we need to create an expression tree (leaves are operands and others are operators)

can draw this tree : (2+3)\*4

# types of traversal

- LVR (left, visit, right) --> in order traversal
<br />
how to know the printed nodes visually ?
<br />

project down each node and read from left to right, this is how the binary tree is represented visually as shown.


![image](https://github.com/user-attachments/assets/8b68607a-96a2-425a-b7f7-d9367194e1f5)

---

- LRV (left, right, visit) --> post order traversal

 --> left first, then right first , then printing the nodes 

 how to deduce the printed nodes visually ? 
 
just in 2 steps : 

**step 1**
for every node , if it doesnot have a right , then project it down, what if it does have a right node? --> wait for it 

**step 2**

for the nodes that have a right node , project it down after its right node.

note that, when projecting the nodes in step 2 , we go from bottom to up level by level.

![image](https://github.com/user-attachments/assets/80d4a03b-e2d0-4145-be93-954e771f2893)

---

- VLR (visit, left, right) --> preorder traversal

 how to deduce the printed nodes visually ? 

will be the opposite of the post order traversal (2 steps)

**step 1**
for every node , if it doesnot have a left, then project it down, what if it does have a left node? --> wait for it 

**step 2**
then we project the nodes that have a left node before its left subtrees 


- note that, when projecting the nodes in step 2 , we go from bottom to up level by level.


![image](https://github.com/user-attachments/assets/83789541-068c-4e8d-b1b2-738d01c9af96)




---
# BFS Tree Structure explanation for the 'whatTasteIsItLike.py' question :

**initial state**


                        food_items
                            │
                ┌───────────┴───────────┐
              fruits               vegetables

Queue Box: ['fruits', 'vegetables']
<br />
Current: []
<br />
Processed: []

---

**step 1**

                        food_items
                            │
                ┌───────────┴───────────┐
              fruits ←             vegetables

Queue Box: ['vegetables', 'tropical', 'temperate']
<br />
Current: 'fruits'
<br />
Processed: ['fruits']

---

**step 2**

                        food_items
                            │
                ┌───────────┴───────────┐
              fruits               vegetables ←
                │                     │
        ┌───────┴───────┐      ┌─────┴─────┐
    tropical        temperate  leafy      root

Queue Box: ['tropical', 'temperate', 'leafy', 'root']
<br />
Current: 'vegetables'
<br />
Processed: ['fruits', 'vegetables']

---

**step 3**

                        food_items
                            │
                ┌───────────┴───────────┐
              fruits               vegetables
                │                     │
        ┌───────┴───────┐      ┌─────┴─────┐
    tropical ←      temperate  leafy      root
        │
    ┌───┴───┐

mango pineapple

Queue Box: ['temperate', 'leafy', 'root', 'mango', 'pineapple']
<br />
Current: 'tropical'
<br />
Processed: ['fruits', 'vegetables', 'tropical']

---

**and so on...**

Logic :

When processing 'apple':
<br />
Queue Box: ['pear', 'spinach', 'kale', 'carrot', 'beet']
<br />
Current: 'apple' (red found!) , since apple is a dict instance and has 'color' in one of its keys... 
<br />
Processed: [..., 'apple']
<br />
Result: ["The apple is sweet."]

<br />
When processing 'beet':
<br />
Queue Box: []
<br />
Current: 'beet' (red found!) , since beet is a dict instance and has 'color' in one of its keys... 
<br />
Processed: [..., 'apple', ..., 'beet']
<br />
Result: ["The apple is sweet.", "The beet is earthy."]

---

The key movements:

Item moves from Queue Box → Current Box
<br />
After processing:
<br />
Item moves to Processed Box
<br />
If it has children, they're added to Queue Box
<br />
If it's red, it adds to Result
---
further explanation : 

So when we say "red found!", we mean:

- val is a dictionary (passed isinstance check)
<br />

- val has a 'color' key (passed 'color' in val check)
<br />

- val['color'] equals 'red' (passed color comparison)

<br />

- This is different from nodes like 'fruits' or 'temperate' which:

-- Are dictionaries but don't have a 'color' key
<br />
-- Have nested dictionaries instead of direct properties







---

<div align="center" style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #e1e4e8;">
  <h3>⚠️ Heads Up!</h3>
  <p><strong>This ReadMe is under constant updates.</strong></p>
  <p>Stay tuned for new notes as I progress. . . 📚💡</p>
</div>

---

# Acknowledgments

> Thanks to Dr.Moustafa Saad, Nidal Fikri
