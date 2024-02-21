class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n,t=len(s),''
        for i in range(n//2):
            t+=s[i]
            if t*(n//(i+1))==s: return True
        return False
