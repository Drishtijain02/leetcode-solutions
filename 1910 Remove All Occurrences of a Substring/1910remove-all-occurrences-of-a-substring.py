class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n=len(s)
        np=len(part)
        while part in s:
            s=s.replace(part,"",1)
        return s








        
        