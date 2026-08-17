import random

class Solution:

    def __init__(self, nums):
        self.hash = {}

        for i in range(len(nums)):
            if nums[i] not in self.hash:
                self.hash[nums[i]] = []

            self.hash[nums[i]].append(i)

    def pick(self, target):
        return random.choice(self.hash[target])