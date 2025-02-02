class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Dictionary to store value -> index mapping

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i # Store index of the current number

        return [] # If no solution is found
    # Time: O(n) because we iterate through the list once
    # Space: O(n) because we store at most n elements in the dictionary