class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                if num > closest:
                    closest = num
        #return min(nums, key=lambda x: (abs(x),-x))
        return closest