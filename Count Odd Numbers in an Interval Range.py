class Solution:
    def countOdds(self, low: int, high: int) -> int:
        od = (j-k)//2
        if k % 2 == 1 or j % 2 == 1:
            od += 1
        return od
        # c=0
        # for i in range(k,j+1):
        #     if i%2==1:
        #         c+=1
        # return c
        
