class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def func(arr,divisor):
            totalans=0
            for i in range(0,len(nums)):
                totalans+=ceil(arr[i]/divisor)
            return totalans
        low=1
        high=max(nums)
        ans=0
        while(low<=high):
            mid=(low+high)//2
            eachans=func(nums,mid)
            if(eachans<=threshold):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans        