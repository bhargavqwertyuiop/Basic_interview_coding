def intersection(nums1,nums2):
    res = []
    for num in nums1:
        if num in nums2 and num not in res:
            res.append(num)
    return res

nums1 = [1,2,3,5]
nums2 = [8,5,3,7]
res = intersection(nums1,nums2)
print(res)