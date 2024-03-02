class Solution:
    def isValid(self, s: str) -> bool:
        # if s=='()'or s=='{}'or s=='[]' or s=='()[]{}': return True
        # else: return False
        stk = []
        stk.append(s[0])
        j=0
        i=1
        while j< len(s)-1:
            stk.append(s[i])
            j+=1

            if s[i]=='}' and s[i-1]=='{' :
                stk.pop(i)
                stk.pop(i-1)
                i-=1
            elif s[i]==')' and s[i-1]=='(':
                stk.pop(i)
                stk.pop(i - 1)
                i -= 1

            elif s[i]==']' and s[i-1]=='[':
                stk.pop(i)
                stk.pop(i - 1)
                i -= 1
            else:
                i+=1

        if not stk :
            return True
        else : return False







