class Solution:
    def beautifulSubsets(self, n: List[int], k: int) -> int:
        c = 0
        # for i in range(len(n)-1):
        #     for j in range(i+1,len(n)-1):
        #         if n[i]-n[j]!=k:
        #             c+=1
        sub = []
        for i in range(1, len(n) + 1):
            sub.extend(combinations(n, i))

        # Iterate through all subsets and count beautiful subsets
        for subset in sub:
            if all(abs(subset[i] - subset[j]) == k for i in range(len(subset)) for j in range(i + 1, len(subset))):
                c += 1

        return c
