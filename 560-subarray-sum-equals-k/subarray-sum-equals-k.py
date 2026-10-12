class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       nhash={}
       nhash[0]=1
       count=0
       summ=0
       for i in range(0,len(nums)):
        summ+=nums[i]
        count+=nhash.get(summ-k,0)
        nhash[summ]=nhash.get(summ,0)+1
       return count
    


       


        