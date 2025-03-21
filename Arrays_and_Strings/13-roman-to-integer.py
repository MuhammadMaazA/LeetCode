class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}

        total = 0  # Inititalize total to accumulate the integer value
        i = 0  # Pointer to traverse the string
        n = len(s)

        while i < n: 
            if (i < n - 1) and (mapping[s[i]] < mapping[s[i+1]]):
                total += mapping[s[i+1]] - mapping[s[i]] 
                i += 2
            else:
                total += mapping[s[i]]
                i += 1

        return total