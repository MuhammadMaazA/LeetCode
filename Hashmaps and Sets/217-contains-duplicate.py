class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) != len(set(nums))
        s = set(nums)
        if len(nums) != len(s):
            return True
        else:
            return False
        
        # Time: O(n) because set() operation is O(n) where n is the number of elements in nums
        # Space: O(n) because we are storing all the elements of nums in a set n elements