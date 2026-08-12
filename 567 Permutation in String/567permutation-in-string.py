class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashhs1 = {}

        # Frequency of characters in s1
        for ch in s1:
            hashhs1[ch] = hashhs1.get(ch, 0) + 1

        n = len(s1)

        # Check every substring of s2 of length n
        for i in range(len(s2) - n + 1):

            hashhs2 = {}

            # Frequency of current substring
            for j in range(i, i + n):
                hashhs2[s2[j]] = hashhs2.get(s2[j], 0) + 1

            # If frequencies are same, permutation exists
            if hashhs1 == hashhs2:
                return True

        return False