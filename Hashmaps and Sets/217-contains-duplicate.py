class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) != len(set(nums))
        s = set(nums)
        if len(nums) != len(s):
            return True
        else:
            return False