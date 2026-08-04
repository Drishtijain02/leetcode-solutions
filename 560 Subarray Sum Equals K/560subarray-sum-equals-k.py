class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        hashh={}
        hashh[0]=1
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            count+=hashh.get(summ-k,0)
            hashh[summ]=hashh.get(summ,0)+1
        return count



        