class Solution:
    def nextPermutation(self, arr):
        n=len(arr)
        pivot=-1
        sub=[];sub1=[]
        for i in range(len(arr)-1,0,-1):
            if arr[i]>arr[i-1]:
                pivot=i-1
                break
        if pivot==-1:
            arr.reverse()
            return
        for j in range(pivot+1,n):
            if arr[j]>arr[pivot]:
                sub.append(arr[j])
            else :
                sub1.append(arr[j])
                
                
        #sub=arr[pivot+1:n]
        sub.sort()
        sub.extend(sub1)
        arr[pivot],sub[0]=sub[0],arr[pivot] #swap
        arr[pivot+1:n]=[]
        
        sub.sort()
        
        arr.extend(sub)
                    
                
        
                
     
            