class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix[0])
        n=len(matrix)
        col=[0]*m
        row=[0]*n
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(0,n):
            for j in range(0,m):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0
        return matrix


        