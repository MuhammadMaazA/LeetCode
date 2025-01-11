class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Initialize a list to keep track of maximum required frequency for each character
        max_freq = [0] * 26  # There are 26 lowercase English letters

        # Iterate over each word in words2 to build the max_freq list
        for word in words2:
            current_freq = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                current_freq[index] += 1
            # Update max_freq with the maximum frequency for each character
            for i in range(26):
                if current_freq[i] > max_freq[i]:
                    max_freq[i] = current_freq[i]

        # List to store the universal words from words1
        universal_words = []

        # Iterate over each word in words1 to check if it is universal
        for word in words1:
            word_freq = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                word_freq[index] += 1

            # Assume the word is universal until proven otherwise
            is_universal = True
            for i in range(26):
                if word_freq[i] < max_freq[i]:
                    is_universal = False
                    break  # No need to check further if one requirement is not met

            # If the word satisfies all frequency requirements, add it to the result
            if is_universal:
                universal_words.append(word)

        return universal_words