
class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
        tiles.sort()

        n = len(tiles)
        ans = 0
        j = 0
        covered = 0

        for i in range(n):
            carpet_end = tiles[i][0] + carpetLen - 1

            while j < n and tiles[j][1] <= carpet_end:
                covered += tiles[j][1] - tiles[j][0] + 1
                j += 1

            total = covered

            if j < n and tiles[j][0] <= carpet_end:
                total += carpet_end - tiles[j][0] + 1

            ans = max(ans, total)

            covered -= tiles[i][1] - tiles[i][0] + 1

            if j < i + 1:
                j = i + 1

        return ans
