class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        j = 0
        for i in s:
            if j == len(t):
                return 0
            if i == t[j]:
                j += 1
                count += 1
        return len(t) - count
