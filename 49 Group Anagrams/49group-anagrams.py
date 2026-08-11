class Solution(object):
    def groupAnagrams(self, strs):
        hashh= {}
        
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word not in hashh:
                hashh[sorted_word] = []
            hashh[sorted_word].append(i)
            
        return list(hashh.values())