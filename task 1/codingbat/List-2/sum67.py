def sum67(nums):
    total = 0
    in_block = False
    for num in nums:
        if num == 6:
            in_block = True
            continue
        if in_block and num == 7:
            in_block = False
            continue
        if not in_block:
            total += num
    return total

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))