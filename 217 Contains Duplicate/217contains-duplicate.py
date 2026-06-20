class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nhash={}
        n=len(nums)
        for i in range(n):
            nhash[nums[i]]=i
        for i in range(n):
            if nums[i] in nhash and nhash[nums[i]]!= i:
                return True
        return False
        