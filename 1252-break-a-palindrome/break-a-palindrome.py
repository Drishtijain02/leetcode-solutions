class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        new=""
        if n==1 or n==0:
            return ""
        for i in range(n//2):
            if palindrome[i]!='a':
                new=palindrome[:i] + 'a' + palindrome[i+1:]
                if new!=new[::-1]:
                    return new
                else:
                    continue
            else:
                continue
        new = palindrome[:-1] + 'b'
        return new

            
        
        