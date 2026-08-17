class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        teen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 0
            if t[i] not in teen:
                teen[t[i]] = 0

            seen[s[i]] = 1 + seen[s[i]] 
            teen[t[i]] = 1 + teen[t[i]]

        if seen == teen:
            return True
        else:
            return False