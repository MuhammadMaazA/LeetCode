class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        
        return result[::-1] # or could do result.reverse() then return result
    # Time: O(n) because we traverse the array 
    # Space: O(n) because we use a list to store the elements and the worst case is all elements are unique so the list will have n elements