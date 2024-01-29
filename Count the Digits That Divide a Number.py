class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)
        cnt=0
        for c in num_str:
            if num%(int(c)) == 0:
                cnt+=1
        return cnt
