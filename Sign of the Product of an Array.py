class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        for k in nums:
            p=p*k
        if p>0:
            return 1
        elif p<0:
            return -1
        else:
            return 0
