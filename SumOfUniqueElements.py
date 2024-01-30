class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        n = Counter(nums)
        sum=0
        for key,val in n.items():
            if val==1:
                sum+=key
          return s
