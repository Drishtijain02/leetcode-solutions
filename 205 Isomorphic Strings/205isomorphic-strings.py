class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashs = {}
        hasht = {}

        for i in range(len(s)):

            if s[i] in hashs:
                if hashs[s[i]] != t[i]:
                    return False
            else:
                hashs[s[i]] = t[i]

            if t[i] in hasht:
                if hasht[t[i]] != s[i]:
                    return False
            else:
                hasht[t[i]] = s[i]

        return True