class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        
        while low<high:
            count=1
            summ=0
            mid=(low+high)//2
            for i in nums:
                if summ+i>mid:
                    count+=1
                    summ=i
                else:
                    summ+=i
            if count>k:
                low=mid+1
            else:
                high=mid
        return low

        

        