class Solution:
    def customSortString(self, order: str, s: str) -> str:
        present = ""
        notpresent = ""
        for i in range(len(order)):
            for j in range(len(s)):
                if order[i]==s[j]: present+=order[i]
                
        for t in range(len(s)):
            if s[t] not in order:
                    notpresent+=s[t]
        return present+notpresent
        
