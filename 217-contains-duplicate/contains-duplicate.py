class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nhash={}
        for i in range(len(nums)):
            nhash[nums[i]]=i
        for i in range(len(nums)):
            check=nhash[nums[i]]
            if nums[i] in nhash and i!=check:
                return True
        return False