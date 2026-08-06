class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashh={}
        for i in range(len(numbers)):
            hashh[numbers[i]]=i
        for i in range(len(numbers)):
            if (target-numbers[i]) in hashh and hashh[target-numbers[i]]!=i:
                return [i+1,hashh.get((target-numbers[i]))+1]
        