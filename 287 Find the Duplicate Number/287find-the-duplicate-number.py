class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        nhash={}
        for i in range(n):
            nhash[nums[i]]=i
        for i in range(n):
            if nums[i] in nhash and nhash[nums[i]]!= i:
                return nums[i]
        return []
        