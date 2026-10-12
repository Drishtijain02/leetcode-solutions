class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nhash={}
        for i in range(len(nums)):
            nhash[nums[i]]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nhash and nhash[diff]!=i:
                return [i,nhash[diff]]
        return []
            