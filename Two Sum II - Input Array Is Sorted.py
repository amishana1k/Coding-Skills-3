class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if n[i]+n[j] == t:
                    return [i+1,j+1]
