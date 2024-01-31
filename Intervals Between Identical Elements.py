class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        N = len(arr)
        lookup = defaultdict(list)


        for index, num in enumerate(arr):
            lookup[num].append(index)


        ans = [0] * N

        def calc(x):
            xArr = lookup[x]

            total = 0

            for i in range(1, len(xArr)):
                total += xArr[i] - xArr[0]

            ans[xArr[0]] = total

            for i in range(1, len(xArr)):
                total += (xArr[i] - xArr[i - 1]) * (i)
                total -= (xArr[i] - xArr[i - 1]) * (len(xArr) - i)
                ans[xArr[i]] = total


        for num in list(lookup.keys()):
            calc(num)


        return ans

  ---------------------OR-----------------------------------

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            s = 0 
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    s += abs(i - j)
            res.append(s)
        return res
