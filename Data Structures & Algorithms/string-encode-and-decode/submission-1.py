class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i)) + '#' + i
        return s


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            count = 0
            while s[j] != "#":
                count += 1
                j += 1
            count = int(s[i:j])
            result.append(s[j + 1 : j + 1 + count])
            i = j + 1 + count
        return result
        

