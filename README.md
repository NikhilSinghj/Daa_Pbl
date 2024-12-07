# Minimum Spanning Tree (MST) Project

This project demonstrates the implementation of Minimum Spanning Tree (MST) algorithms (Prim's and Kruskal's) for designing cost-effective networks. The program calculates the MST of a graph and outputs its total cost and edges.

---

## Prerequisites

### 1. Python Installed
Ensure Python 3.x is installed on your system. Download it from [python.org](https://www.python.org/).

### 2. Required Libraries
Install the following Python libraries if not already installed:

```bash
pip install -r requirements.txt
```

---

## Steps to Run the Program

### 1. Clone or Download the Repository
- Clone this repository or download the script to your local machine.

### 2. Choose the Algorithm
- Decide whether to run Prim's or Kruskal's algorithm.

### 3. Run the Program
1. **Navigate to the directory** containing the program file:
   ```bash
   cd path/to/project
   ```
2. **Execute the script** using Python:
   ```bash
   python mst.py
   ```

---

## Program Overview

### **Input**
The graph is represented with:
- **Vertices**: Nodes (e.g., cities or stations).
- **Edges**: Weighted connections (e.g., cost of roads or cables).

### **Output**
- The MST edges and their total cost.

---

## Example

### Input
A graph with 5 vertices and the following weighted edges:
```
0 - 1 (weight: 2)
0 - 3 (weight: 6)
1 - 2 (weight: 3)
1 - 3 (weight: 8)
1 - 4 (weight: 5)
2 - 4 (weight: 7)
```

### Output
```
MST Cost: 16
MST Edges: [(0, 1), (1, 2), (1, 4), (0, 3)]
```

---




