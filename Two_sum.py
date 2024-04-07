def twoSum(nums, target):
    indices = {}
    for i, num in enumerate(nums):
        left = target -  num
        if left in indices:
            return (indices[left], i)
        else:
            indices[num] = i
    return []