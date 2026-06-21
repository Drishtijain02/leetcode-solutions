class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nhash={}
        n=len(nums1)
        result=[]
        for i in range(n):
            nhash[nums1[i]]=i
        for i in range(len(nums2)):
            if nums2[i] in nhash and nums2[i] not in result:
                result.append(nums2[i])
        return result
