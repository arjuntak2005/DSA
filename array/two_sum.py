"""
Two Sum: 
- You are given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution, and you 
may not use the same element twice.
- You can return the answer in any order.
"""
# Optimal solution.
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def two_sum(nums, target):
    map = {}
    for i in range(len(nums)):
        num2 = target - nums[i]
        if num2 in map:
            return [map[num2], i]
        map[nums[i]] = i
    return None


# Brute Force optimised solution.
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def two_sum_func(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# Test Cases
if __name__ == "__main__":
    print("Two Sum: ")
    problems = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 8, 12, 19], 20)
    ]
    for nums, target in problems:
        print(f"Problem: nums = {nums}, target = {target}")
        print(f"Solution: {two_sum(nums, target)}")
        print()
