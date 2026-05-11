class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        r=n-1
        l=0
        maxi=0
        while(l<r):
            diff=r-l
            area=min(height[r],height[l])*diff
            maxi=max(area,maxi)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxi
        