class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        prev=intervals[0]
        n=len(intervals)
        for i in range(1,n):
            if intervals[i][0]<= prev[1]:
                prev[1]=max(prev[1],intervals[i][1])
            else:
                result.append(prev)
                prev=intervals[i]
        result.append(prev)
        return result
                
        