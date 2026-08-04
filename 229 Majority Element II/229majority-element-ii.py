class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashh={}
        freq=0
        n=len(nums)
        result=set()
        listt=[]
        for i in range(n):
            freq=hashh.get(nums[i],0)+1
            hashh[nums[i]]=freq
            if freq>(n//3):
                result.add(nums[i])
        listt=list(result)
        return listt

        
        