class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = nums[0]

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            maxx = max(maxx, product)
            if product == 0:
                product = 1

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            maxx = max(maxx, product)
            if product == 0:
                product = 1
        return maxx
        

        