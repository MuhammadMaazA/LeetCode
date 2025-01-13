class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        
        freq = Counter(s)
        ans = 0
        
        for char, count in freq.items():
            if count == 0:
                continue
            if count % 2 == 1:
                # odd frequency -> 1 remains
                ans += 1
            else:
                # even frequency -> 2 remain
                ans += 2
        
        return ans
