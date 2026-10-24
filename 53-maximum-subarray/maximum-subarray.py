class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=0
        maxx=float('-inf')
        for i in range(len(nums)):
            current+=nums[i]
            maxx=max(maxx,current)
            if current<0:
                current=0
        return maxx