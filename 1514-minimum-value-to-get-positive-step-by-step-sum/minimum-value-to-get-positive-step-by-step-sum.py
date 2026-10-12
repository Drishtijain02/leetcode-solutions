class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        k = 1

        while True:
            count = 0
            summ = k + nums[0]

            if summ >= 1:
                count += 1

            for i in range(1, len(nums)):
                summ = summ + nums[i]

                if summ < 1:
                    break

                count += 1

            if count == len(nums):
                return k

            k += 1