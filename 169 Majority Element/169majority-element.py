class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         l=len(nums)
         nums.sort()
         return nums[l//2]
                