def twoSum(nums, target):
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i

    return []

print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 2, 4], 6))       # [1, 2]