class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left + 1, right + 1]
            elif summ < target:
                left += 1
            else:
                right -= 1
        # Time: O(n) because we traverse the array
        # Space: O(1) because we do not use any extra space
        