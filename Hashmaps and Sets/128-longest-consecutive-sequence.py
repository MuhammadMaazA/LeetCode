class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        
        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest
    
    # Time: O(n) because we traverse the array only once
    # Space: O(n) because we use a set to store the elements and the worst case is all elements are unique so the set will have n elements