def max_end3(nums):
    m = max(nums[0], nums[2])
    return [m, m, m]

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))