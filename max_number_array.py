def find_max(nums):
    max_num = float('-inf')         #-inf
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

nums = [1,2,3,4,5,7]
res = find_max(nums)
print(res)