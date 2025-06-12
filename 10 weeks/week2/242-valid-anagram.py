class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
    # Time: O(n) where n is the length of the strings, we traverse each string once
    # Space: O(n) where n is the length of the strings, for the Counter dictionaries
        # This solution is efficient because it counts the frequency of each character in both strings and compares the counts