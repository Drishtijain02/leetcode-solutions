class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for x in nums1:
            idx = nums2.index(x)
            nxt = -1

            for i in range(idx + 1, len(nums2)):
                if nums2[i] > x:
                    nxt = nums2[i]
                    break

            ans.append(nxt)

        return ans