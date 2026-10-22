
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        def check(arr):
            return all(arr[i] == (arr[0] + i) % n for i in range(n))

        ans = float('inf')

        if check(nums):
            k = (n - nums[0]) % n
            ans = min(ans, k, n - k + 2)

        rev = nums[::-1]
        if check(rev):
            k = (n - rev[0]) % n
            ans = min(ans, k + 1, n - k + 1)

        return ans if ans != float('inf') else -1
