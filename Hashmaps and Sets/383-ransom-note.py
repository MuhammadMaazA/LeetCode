class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = [0] * 26
        for char in magazine:
            index = ord(char) - ord('a') # ord() returns the unicode code of a character and here we are subtracting the unicode code of 'a' to get the index of the character in the list
            magazine_count[index] += 1
        
        for char in ransomNote:
            index = ord(char) - ord('a')
            magazine_count[index] -= 1
            if magazine_count[index] < 0:
                return False
        return True
    