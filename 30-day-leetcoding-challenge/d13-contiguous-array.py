class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total_zeros = len(nums) - sum(nums)
        total_ones = sum(nums)
        
        if total_zeros == total_ones:
            return len(nums)
        
        if total_zeros == 0 or total_ones == 0:
            return 0
        
        res = len(nums)
        
        zeros_start, zeros_end, ones_start, ones_end = [], [], [], []
        cur_zeros, cur_ones = 0, 0
        
        for x in nums:
            if x == 0:
                cur_zeros += 1
            else:
                cur_ones += 1
            zeros_start.append(cur_zeros)
            ones_start.append(cur_ones)
        
        cur_zeros, cur_ones = 0, 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                cur_zeros += 1
            else:
                cur_ones += 1
            zeros_end.append(cur_zeros)
            ones_end.append(cur_ones)            
            
        # print(zeros_start, zeros_end, ones_start, ones_end)
        start, end = 0, res - 1
        
        if total_zeros > total_ones:
            if zeros_start[res//2] >= zeros_end[res//2]:
                while total_zeros > total_ones and nums[start] == 0:
                    start += 1
                    total_zeros -= 1
            else:
                while total_zeros > total_ones and nums[end] == 0:
                    end -= 1
                    total_zeros -= 1
            return self.findMaxLength(nums[start:(end + 1)])
        elif total_zeros < total_ones:
            if ones_start[res//2] >= ones_end[res//2]:
                while total_ones > total_zeros and nums[start] == 1:
                    start += 1
                    total_ones -= 1
            else:
                while total_ones > total_zeros and nums[end] == 1:
                    end -= 1
                    total_ones -= 1
            return self.findMaxLength(nums[start:(end + 1)])   
        