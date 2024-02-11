class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r=[]
        n = Counter(nums)
        for i, v in n.items():
            if v >=2:
                r.append(i)
        return r
        
