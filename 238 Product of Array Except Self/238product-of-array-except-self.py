class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        
        pref=1
        for i in range(n):
            result[i]=pref
            pref*=nums[i]
        suff=1
        for j in range(n-1,-1,-1):
            result[j]*=suff
            suff*=nums[j]
        return result

        