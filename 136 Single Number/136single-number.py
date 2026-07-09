class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        hashn={}
        for i in range(n):
            hashn[nums[i]]=hashn.get(nums[i],0)+1
        for j in range(n):
            if hashn[nums[j]]==1:
                return nums[j]


        