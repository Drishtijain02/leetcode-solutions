class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashn={}
        n=len(nums)
        for i in range(0,n+1):
            hashn[i]=i
        for j in range(n+1):
            if hashn[j] not in nums:
                return hashn[j]




        