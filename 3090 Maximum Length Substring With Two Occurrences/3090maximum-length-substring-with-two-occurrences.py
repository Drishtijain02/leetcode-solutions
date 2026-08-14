class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        hashh = {}
        left = 0
        ans = 0

        for right in range(len(s)):

            # Add current character
            hashh[s[right]] = hashh.get(s[right], 0) + 1

            # If current character occurs more than 2 times
            while hashh[s[right]] > 2:

                hashh[s[left]] -= 1
                left += 1

            # Window is now valid
            ans = max(ans, right - left + 1)

        return ans