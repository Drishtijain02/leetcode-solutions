class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        currentsumm=0
        for i in nums:
            currentsumm=currentsumm+i
            if currentsumm>maxSum:
                maxSum=currentsumm
            if currentsumm<0:
                currentsumm=0
        return maxSum

        