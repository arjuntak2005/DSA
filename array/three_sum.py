# Brute Force
def three_sum(nums):
    res = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in res:
                        res.append(triplet)
    return res