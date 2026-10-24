class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        j=1
        while True:
            summ=j+nums[0]
            count=0
            if summ >= 1:
                count += 1
            for i in range(1,len(nums)):
                summ+=nums[i]
                if summ<1:
                    break
                count+=1
            if count==len(nums):
                return j
            j=j+1
            
        
        
            
                

