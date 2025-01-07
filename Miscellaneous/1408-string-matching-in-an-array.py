class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Sort the words by length in descending order
        words_sorted = sorted(words, key=lambda x: -len(x))
        result = []
        
        for i in range(len(words_sorted)):
            current_word = words_sorted[i]
            for j in range(len(words_sorted)):
                if i == j:
                    continue  # Skip the same word
                if current_word in words_sorted[j]:
                    result.append(current_word)
                    break  # No need to check other words
        return result