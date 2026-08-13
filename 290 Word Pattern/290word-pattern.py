class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashs = {}
        hasht = {}

        sl = s.split()

        
        if len(pattern) != len(sl):
            return False

        for i in range(len(sl)):

            
            if sl[i] in hashs:
                if hashs[sl[i]] != pattern[i]:
                    return False
            else:
                hashs[sl[i]] = pattern[i]

            
            if pattern[i] in hasht:
                if hasht[pattern[i]] != sl[i]:
                    return False
            else:
                hasht[pattern[i]] = sl[i]

        return True