class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=set()
        freq=0
        nhash={}
        for i in range(len(nums)):
            freq=nhash.get(nums[i],0)+1
            if freq>((len(nums))//3):
                result.add(nums[i])
            nhash[nums[i]]=freq
        result=list(result)
        return result
        
        