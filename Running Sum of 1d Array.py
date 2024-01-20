class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j=0
        res=[]
        for i in nums:
            j+=i
            res.append(j)
        return res
