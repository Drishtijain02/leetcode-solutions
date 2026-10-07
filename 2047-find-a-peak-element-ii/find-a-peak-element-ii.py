class Solution:
    def findPeakGrid(self, mat):
        m, n = len(mat), len(mat[0])
        low, high = 0, m - 1

        while low <= high:
            mid = (low + high) // 2
            col = max(range(n), key=lambda j: mat[mid][j])

            up = mat[mid - 1][col] if mid > 0 else -1
            down = mat[mid + 1][col] if mid < m - 1 else -1

            if mat[mid][col] > up and mat[mid][col] > down:
                return [mid, col]
            elif up > mat[mid][col]:
                high = mid - 1
            else:
                low = mid + 1