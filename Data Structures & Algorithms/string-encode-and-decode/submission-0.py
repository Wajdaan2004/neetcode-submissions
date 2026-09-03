class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            x = str(len(i))
            s += x + '#' + i 
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j + 1 + length])
            i = j + 1 + length
        return result
        

