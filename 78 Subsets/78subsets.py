class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, subset):
            # Store the current subset
            result.append(subset[:])

            # Try adding each remaining element
            for i in range(index, len(nums)):
                subset.append(nums[i])          # Choose
                backtrack(i + 1, subset)        # Explore
                subset.pop()                    # Unchoose

        backtrack(0, [])
        return result