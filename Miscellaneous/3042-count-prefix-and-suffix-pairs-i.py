class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        
        # Iterate over all possible pairs (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                prefix = words[i]
                target = words[j]
                
                if target.startswith(prefix) and target.endswith(prefix):
                    count += 1
                    
        return count