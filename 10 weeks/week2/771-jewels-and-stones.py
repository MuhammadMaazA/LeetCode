class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for stone in stones:
            if stone in jewels:
                ans += 1
        return ans
    # Time: O(n * m) where n is the length of stones and m is the length of jewels
    # Space: O(1) we only use a few variables regardless of input size
        s = set(jewels)
        count = 0
        for letter in stones:
            if letter in s:
                count += 1
        return count
    # Time: O(n + m) where n is the length of stones and m is the length of jewels
    # Space: O(m) where m is the length of jewels, for the set
        # This is more efficient than the previous solution because checking membership in a set is O(1) on average