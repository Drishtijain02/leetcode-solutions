class Solution(object):
    def isPalindrome(self, x):
        temp=x
        rev=0
        while(temp>0):
            d=temp%10
            rev=rev*10 +d
            temp=temp//10
        if(rev==x):
            return True
        else:
            return False

            
