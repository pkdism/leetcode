class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            complement = target-nums[i]
            if complement in nums[(i+1):]:
                return [i, nums[(i+1):].index(complement)+i+1]
        return None
