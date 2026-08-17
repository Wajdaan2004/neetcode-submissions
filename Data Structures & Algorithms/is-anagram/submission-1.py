class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
            elif s[i] in dict_s:
                dict_s[s[i]] += 1
            if t[i] not in dict_t:
                dict_t[t[i]] = 1
            elif t[i] in dict_t:
                dict_t[t[i]] += 1
        for i in range(len(s)):
            if s[i] not in dict_t:
                return False
            x = dict_s[s[i]]
            y = dict_t[s[i]]
            if x != y :
                return False
        return True
