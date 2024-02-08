class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        pairs = []
        for num in nums:
            complement = target - num
            if complement in hashmap:
                pairs.append([num, complement])
            hashmap[num] = 1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = {}
        for i in range(len(nums)):
            first = nums[i]
            two_sum_res = self.twoSum(nums[(i+1):], -first)
            if two_sum_res:
                for pair in two_sum_res:
                    triplets[tuple(sorted([first, pair[0], pair[1]]))] = 1
        return triplets.keys()
