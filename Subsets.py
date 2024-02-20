class Solution:
    def subsets(self, n: List[int]) -> List[List[int]]:
        b=[[]]
        
        l=len(n)
        if l!=1:
            for i in range(l):
                b.append([n[i]])
                for j in range(i+1,l):
                    b.append([n[i],n[j]])
        c=b
        if n not in b: 
            c=b+[n]
        return c
