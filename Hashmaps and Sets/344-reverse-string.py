class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left] # swap characters
            left += 1
            right -= 1
        # Time: O(n) because we traverse the array
        # Space: O(1) because we do not use any extra space