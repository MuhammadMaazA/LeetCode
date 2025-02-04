class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Using Boyer Moore Voting Algorithm 
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate, count = num, 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    
    # Time: O(n) because we traverse the array only once
    # Space: O(1) because we use only two variables candidate and count