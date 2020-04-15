"""
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = 0
        for x in nums:
            if x == 0:
                zeros += 1
        if zeros > 1:
            return [0]*n
        elif zeros == 0:
            res = []
            prod = 1
            for x in nums:
                prod = prod*x
            for x in nums:
                res.append(prod//x)
            return res
        else:
            prod = 1
            res = []
            for x in nums:
                if x != 0:
                    prod = prod*x
            for x in nums:
                if x == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
