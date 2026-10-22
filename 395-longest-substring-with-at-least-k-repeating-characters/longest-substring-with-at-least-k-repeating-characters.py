class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for target in range(1, 27):
            freq = {}
            left = 0
            unique = 0
            countK = 0
            for right in range(n):
                ch = s[right]
                freq[ch] = freq.get(ch, 0) + 1
                if freq[ch] == 1:
                    unique += 1
                if freq[ch] == k:
                    countK += 1
                while unique > target:
                    c = s[left]
                    if freq[c] == k:
                        countK -= 1
                    freq[c] -= 1
                    if freq[c] == 0:
                        unique -= 1
                        del freq[c]
                    left += 1
                if unique == target and unique == countK:
                    ans = max(ans, right - left + 1)
        return ans