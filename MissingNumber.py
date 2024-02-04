class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sorted(nums)
        for i in range(0,len(n)):
            if i not in nums:
                return i
