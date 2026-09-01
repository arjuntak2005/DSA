"""
Problem: Largest integers in the array
Approach: Compare each element of array/list with the largest.
Time Complexity: O(n)
Space Complexity: O(1)
"""


def largest_int(array):
    """
    array: list[int]
    returns: largest number in the array
    """
    largest = array[0]
    for i in range(0, len(array)):
        if largest < array[i]:
            largest = array[i]
    return largest


if __name__ == "__main__":
    print(largest_int([1, 2, 4, 7, 5]))  # Expected: 7
    print(largest_int([3, 2, 4, 1, 2, 9]))  # Expected: 9
