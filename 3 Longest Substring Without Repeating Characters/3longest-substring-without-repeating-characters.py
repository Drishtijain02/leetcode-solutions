class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashh = {}
        left = 0
        maxx = 0

        for right in range(len(s)):
            if s[right] in hashh and hashh[s[right]] >= left:
                left = hashh[s[right]] + 1

            hashh[s[right]] = right
            maxx = max(maxx, right - left + 1)

        return maxx