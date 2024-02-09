class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=[]
        a = {}
        for i in strs:
            srted = ''.join(sorted(i))
            if srted not in a:
                a[srted] = [i]
            # If key is already present, append the word to the existing list
            else:
                a[srted].append(i)
        for d in a.values():
            r.append(d)       
        return r
