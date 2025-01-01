from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        if len(word1) == len(word2):
            return ''.join(word1[i] + word2[i] for i in range(len(word1)))
        if len(word1) > len(word2):
            return ''.join(word1[i] + word2[i] for i in range(len(word2))) + word1[len(word2):]
        return ''.join(word1[i] + word2[i] for i in range(len(word1))) + word2[len(word1):]
        '''
        '''
        merged = [a+b for a, b in zip(word1, word2)]
        merged.append(word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):])
        return ''.join(merged)
        '''
        merged = []
        for a, b in zip_longest(word1, word2, fillvalue=''):
            merged.append(a)
            merged.append(b)
        return ''.join(merged)