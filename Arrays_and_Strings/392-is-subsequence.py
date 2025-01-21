class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if s == '': return True
        if S > T: return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S - 1:  # stops as soon as all the characters of s are matched
                    return True 
                j += 1
        return False
        