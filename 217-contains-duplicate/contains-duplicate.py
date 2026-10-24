class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashh={}
        for i in range(len(nums)):
            hashh[nums[i]]=i
        for i in range(len(nums)):
            check=hashh.get(nums[i],0)
            if check!=0 and check!=i:
                return True
        return False