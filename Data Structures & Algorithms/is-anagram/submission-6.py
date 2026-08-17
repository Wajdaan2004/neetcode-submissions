class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        teen = {}
        for i in range(len(s)):
            seen[s[i]] = 1 + seen.get(s[i], 0) 
            teen[t[i]] = 1 + teen.get(t[i], 0)

        if seen == teen:
            return True
        else:
            return False