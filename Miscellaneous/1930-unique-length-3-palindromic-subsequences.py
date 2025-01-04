class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        n = len(s)
        
        # Iterate over all lowercase letters
        for c in range(26):
            char = chr(ord('a') + c)
            left = s.find(char)
            right = s.rfind(char)
            
            # Check if the character appears at least twice
            if left == -1 or left == right:
                continue
            
            # Extract the substring between the first and last occurrence
            middle_substring = s[left+1:right]
            
            # Use a set to count unique characters in the middle substring
            unique_chars = set(middle_substring)
            
            # Each unique character forms a unique palindromic subsequence 'c_b_c'
            result += len(unique_chars)
        
        return result