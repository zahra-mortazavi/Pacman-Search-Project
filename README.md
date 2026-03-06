
---

# 🟡 Pacman Search Project

This project implements several **search algorithms** to solve pathfinding problems in the **Pacman game environment**.
The goal is to find a path for Pacman to reach the target using different search strategies.

---

# 📌 Implemented Algorithms

The following algorithms are implemented in this project:

* **Depth First Search (DFS)**
* **Uniform Cost Search (UCS)**
* **A* Search (A-Star)**

Each algorithm is implemented using appropriate data structures such as **Stack** and **Priority Queue**.

---

# 🔎 Algorithms Explanation

## 1️⃣ Depth First Search (DFS)

The **DFS algorithm** is implemented using a **Stack**.
It explores as deep as possible along each branch before backtracking.

### Features

* Uses a **Stack**
* Maintains an `explored` set to avoid revisiting states
* Reconstructs the final path using the `help` dictionary

---

## 2️⃣ Uniform Cost Search (UCS)

The **UCS algorithm** is used to find the **lowest-cost path** to the goal.

### Features

* Uses a **Priority Queue**
* Expands nodes based on the **lowest path cost**
* Stores the cost of each node in the `help` dictionary

---

## 3️⃣ A* Search

The **A*** algorithm combines the **path cost** and a **heuristic function** to find a more optimal solution.

### Priority Formula

```
f(n) = g(n) + h(n)
```

Where:

* `g(n)` = cost of the path so far
* `h(n)` = heuristic value

In this project, the **`cornersHeuristic`** function is used for the **Corners Problem**.

---

# ▶️ Running the Program

To run the **A*** algorithm on the **Corners Problem**, use the following command:

```bash
python pacman.py -l HardCorner -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic
```

---

# 🗺️ Available Maps

The game map can be one of the following:

* `SimpleCorner`
* `BigCorner`
* `HardCorner`

### Example

```bash
python pacman.py -l BigCorner -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic
```

---

# 🧩 Code Structure

Main functions in the project:

| Function             | Description                         |
| -------------------- | ----------------------------------- |
| `depthFirstSearch`   | Implementation of DFS               |
| `breadthFirstSearch` | Implementation of BFS (in progress) |
| `uniformCostSearch`  | Implementation of UCS               |
| `aStarSearch`        | Implementation of A* algorithm      |
| `nullHeuristic`      | Base heuristic returning 0          |

---

# 🔤 Abbreviations

For convenience, the following shortcuts are available:

```python
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
```

---

# 🎯 Project Goal

The main objective of this project is to gain familiarity with:

* Classical **search algorithms**
* Designing **agents for intelligent environments**
* Using **heuristics to optimize search**

---

# 🎓 Academic Context

Developed as part of a **Fundamentals and applications of artificial intelligence course**

📅 Fall 2024

---
