class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def func(arr,cap):
            day=1
            load=0
            for i in range(0,len(arr)):
                if (load+arr[i]>cap):
                    day+=1
                    load=arr[i]
                else:
                    load+=arr[i]
            return day
        low=max(weights)
        high=sum(weights)
        ans=0
        while(low<=high):
            mid=(low+high)//2
            reqday=func(weights,mid)
            if reqday<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans        