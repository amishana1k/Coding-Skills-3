class Solution:
    def maximumSwap(self, num: int) -> int:
        n =[int(digit) for digit in str(num)]
        j=1
        for i in range(len(n)):
            while j<len(n):
                if n[j]>n[i]:
                    n[i],n[j]=n[j],n[i]
                    return int(''.join(map(str, n)))
                j+=1
            j+=2
        return num
        
