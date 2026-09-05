"""
Problem: You are given a 0-indexed integer array nums of even length consisting of an equal 
number of positive and negative integers.
You should return the array of nums such that the array follows the given conditions:
- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in nums is preserved.
- The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

#Brute Force
Time Complexity: O(n)
Auxiliary Space: O(n)
Total Space: O(n)
"""


def rearrange_array(nums):
    pos = []
    neg = []

    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    ans = []
    for i in range(len(pos)):
        ans.append(pos[i])
        ans.append(neg[i])

    return ans


# Test Cases
if __name__ == "__main__":
    print("Rearrange Array Elements by Sign: ")
    problems = [
        [3, 1, -2, -5, 2, -4],
        [-1, 1]
    ]
    for problem in problems:
        print(f"Problem: {problem}")
        print(f"Solution: {rearrange_array(problem)}")
        print()
