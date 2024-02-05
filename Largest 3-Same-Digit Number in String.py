class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count=0
        prev='X'
        maxd=' '
        for c in num:
            if c==prev: count+=1
            else: count=1
            if count==3: maxd=max(c, maxd)
            prev=c
        if maxd==' ': return ""
        return maxd*3

---------------------OR---------------------------
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        ans=""
        for i in range(n):
            if i+2<n and num[i]==num[i+1] and num[i]==num[i+2]:
                ans=max(ans,num[i:i+3])
        return ans    
