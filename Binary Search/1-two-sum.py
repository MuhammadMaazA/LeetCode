class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
    # Time: O(n^2) where n is the length of nums, we check every pair
    # Space: O(1) we only use a few variables regardless of input size

    # Optimized solution using a dictionary
        h = {}
        n = len(nums)
        for i, x in enumerate(nums):
            y = target - x:
            if y in h:
                return [h[y], i]
            else:
                h[x] = i
    # Time: O(n) where n is the length of nums, we traverse the list once
    # Space: O(n) where n is the length of nums, for the dictionary
    