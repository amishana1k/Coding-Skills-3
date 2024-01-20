class Solution:
    def firstUniqChar(self, s: str) -> int:
        charcount = Counter(s)
        
        for i, char in enumerate(s):
            if charcount[char] == 1:
                return i

        return -1
