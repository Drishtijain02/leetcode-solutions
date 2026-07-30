class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[[1],[1,1]]
        prev_arr=[1,1]
        if(numRows==1): 
            return [[1]]
        elif(numRows==2): 
            return [[1],[1,1]]
        for i in range(3,numRows+1):
            curr_arr=[0]*i
            for j in range(i):
                if(j==0 or j==i-1):
                    curr_arr[j]=1
                else:
                    curr_arr[j]=prev_arr[j-1]+prev_arr[j]
            output.append(curr_arr)
            prev_arr=curr_arr
        return output