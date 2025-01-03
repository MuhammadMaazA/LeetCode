class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        count = 0
        
        # Iterate through the array up to the second last element
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            remaining_sum = total_sum - prefix_sum
            
            # Check if the current split is valid
            if prefix_sum >= remaining_sum:
                count += 1
                
        return count

        