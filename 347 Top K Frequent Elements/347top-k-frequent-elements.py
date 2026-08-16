class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashh = {}

        for num in nums:
            hashh[num] = hashh.get(num, 0) + 1

        ans = sorted(hashh, key=hashh.get, reverse=True)

        return ans[:k]