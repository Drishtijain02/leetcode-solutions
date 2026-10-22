class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=(n*m)-1
        while(low<=high):
            mid=(low+high)//2
            row=int(mid/n)
            col=int(mid%n)
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]>target):
                high=mid-1
            else:
                low=mid+1
        return False
