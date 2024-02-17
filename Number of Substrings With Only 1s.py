class Solution:
    def numSub(self, s: str) -> int:
        c = 0
        n = len(s)
        i = 0
        k = 1
        
        while k <= n:
            while i <= n - k:
                if s[i:i+k] == '1' * k:
                    c += 1
                i += 1
            k += 1
            i = 0

        return c
