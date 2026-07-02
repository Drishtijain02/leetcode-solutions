class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result=""
        n=len(strs)
        first=strs[0]
        last=strs[n-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return result
            result+=first[i]
        return result


        