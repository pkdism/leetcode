class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        skip = 0
        final_product = [1]*n
        pre_product, post_product = 1, 1
        for i in range(n):
            final_product[i] = pre_product
            pre_product *= nums[i]
        for i in range(n-1, -1, -1):
            final_product[i] = final_product[i]*post_product
            post_product *= nums[i]
        return final_product