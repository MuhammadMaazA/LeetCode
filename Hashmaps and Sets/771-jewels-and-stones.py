class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for letter in stones:
            if letter in s:
                count += 1
        return count
    
    # Time: O(n+m)
    # Space: O(1)
    # checking membership in set is on average O(1) compared to O(m) for a string
    