class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            hashh = {}

            for j in range(i, len(s)):
                hashh[s[j]] = hashh.get(s[j], 0) + 1

                maxf = max(hashh.values())
                minf = min(hashh.values())

                ans += maxf - minf

        return ans