class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Condition 1: k should not exceed the number of characters in s
        if k > len(s):
            return False
        
        # Initialize a list to count frequencies of each lowercase letter ('a' to 'z')
        freq = [0] * 26  # 26 letters in the English alphabet
        
        # Count the frequency of each character in s
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # Count the number of characters with odd frequencies
        odd_count = 0
        for count in freq:
            if count % 2 != 0:
                odd_count += 1
        
        # Condition 2: The number of odd frequencies should not exceed k
        return odd_count <= k
