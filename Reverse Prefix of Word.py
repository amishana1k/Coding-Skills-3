class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        pre = ""
        rest = ""
        for i in range(len(word)):
            if ch == word[i]:
                pre = word[:i+1]
                break
        else:
            return word
        rest = word[i+1:]
        pre = pre[::-1]
        return pre+rest

        

        
