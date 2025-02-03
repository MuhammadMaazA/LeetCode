class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            # Create a frequency count for each string
            count = [0] * 26 # Array of size 26 for lowercase English letters
            for c in s:
                count[ord(c) - ord('a')] += 1 # Update frequence of each character

            # Use the tuple of the frequency count as the key
            key = tuple(count)
            anagrams_dict[key].append(s)

        # Return grouped anagrams as a list of lists
        return list(anagrams_dict.values())
    # Time: O(n*m) where n is the number of strings and m is the max length of a string
    # Space: O(n*m) because we store n strings of length m in the dictionary
    