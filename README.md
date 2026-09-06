# 📊 DSA Practice Log

Personal Data Structures & Algorithms practice repository solved in Python, organized by topic, tracked here for quick revision.

**Number of Questions:** 6 solved
---

## Arrays

| Problem | File | Pattern | Time | Space | Status | Notes |
|---|---|---|---|---|---|---|
| [Largest in Array](https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1) | [`find_largest_int.py`](array/find_largest_int.py) | Traversal | O(n) | O(1) | ✅ | Optimal solution |
| [Majority Element](https://leetcode.com/problems/majority-element/description/) | [`majority_element.py`](array/majority_element.py) | Voting | O(n) | O(1) | 🔁 | Optimal solution using the Boyer-Moore Voting Algorithm |
| [Array Leaders](https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1) | [`array_leaders.py`](array/array_leaders.py) | Traversal | O(n) | O(n) | ✅ | Optimal solution |
| [Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/) | [`rearrange_by_sign.py`](array/rearrange_by_sign.py) |  | O(n) | O(n) | ✅ | Brute Force |
| [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/) | [`spiral_matrix.py`](array/spiral_matrix.py) |  | O(-) | O(-) | ❌ | Pending |
| [Rotate Image](https://leetcode.com/problems/rotate-image/description/) | [`rotate-image.py`](array/rotate-image.py) |  | O(-) | O(-) | ❌ | Pending |

C:\Users\Arjun\Documents\Github-DSA\DSA\array\rotate_matrix_90_degrees.py
## How to Use This Repo
1. Each topic has its own folder with one `.py` file per problem.
2. Every file has a docstring: problem statement, approach, complexity.
3. Multiple approaches to the same problem live in the same file as separate functions.
4. This README is the master index updated right after solving each problem.
    | Symbol | Meaning |
    |---|---|
    | ✅ | Solved |
    | 🔁 | Revisit |
    | ❌ | Struggled |
---
Each `.py` file contains:
- A docstring with the problem statement, approach, and complexity
- One function per approach (e.g. brute force + optimal in the same file)
- A test block at the bottom (`if __name__ == "__main__":`) demonstrating the solution

