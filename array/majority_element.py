
# 1. Brute-Force Solution:
"""
Time: O(n^2)
Space: O(1)
"""


def majority_element_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_count = 0
    majority_element = -1
    for i in range(0, len(nums)):
        c = count(nums[i], nums)
        if c > max_count:
            max_count = c
            majority_element = nums[i]
    if majority_element == -1:
        return None
    return majority_element


def count(elem, nums):
    """
    elem: int
    nums: list[int] 
    returns: int, number of times elem present in nums array.
    """
    count = 0
    for i in nums:
        if i == elem:
            count += 1
    return count


# 2. Better Solution (Space for Time Trade-off)
"""
Time: O(2n) ~= O(n)
Space: O(n)
"""


def majority_element_2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = {}
    for i in range(0, len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
        else:
            count[nums[i]] += 1

    max_val = 0
    req_key = None
    for key, val in count.items():
        if val > max_val:
            max_val = val
            req_key = key
    return req_key


# Optimal Solution
# working on it..
if __name__ == "__main__":
    print("Majority Element: ")
    problems = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [],
        [3, 2, 1, 0, 0, 0]
    ]
    for problem in problems:
        print(f"Problem: {problem}")
        print(f"Solution: {majority_element_2(problem)}")
        print()
