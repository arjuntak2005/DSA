"""
Problem: You are given an array arr of positive integers. 
Your task is to find all the leaders in the array. An element is considered 
a leader if it is greater than or equal to all elements to its right. 
The rightmost element is always a leader.

Approach: -
1. Traverse the array from right to left.
2. Keep track of the maximum element encountered so far.
3. If the current element is greater than the maximum, it is a leader

Note: Order of elements in solution may be different. 

Time Complexity: O(n)
Auxiliary Space: O(1)
Total Space: O(n)
"""
# Optimal Solution


def leaders_2(arr):
    leaders = []
    elem = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > elem:
            elem = arr[i]
            leaders.append(elem)
    return leaders


# Brute Force
"""
Time Complexity: O(n^2)
Space Complexity: O(n)
Auxiliary Space: O(1)
"""


def leaders_1(arr):
    leaders = []
    for i in range(0, len(arr)):
        is_leader = True
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                is_leader = False
        if is_leader:
            leaders.append(arr[i])
    return leaders


# Test Cases
if __name__ == "__main__":
    print("Array Leaders: ")
    problems = [
        [16, 17, 4, 3, 5, 2],
        [10, 4, 2, 4, 1],
        [5, 10, 20, 40],
        [30, 10, 10, 5]
    ]
    for problem in problems:
        print(f"Problem: {problem}")
        print(f"Solution: {leaders_2(problem)}")
        print()
