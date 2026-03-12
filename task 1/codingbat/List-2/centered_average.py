def centered_average(nums):
    nums_sorted = sorted(nums)
    trimmed = nums_sorted[1:-1] 
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))