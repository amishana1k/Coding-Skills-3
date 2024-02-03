from collections import deque

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = deque()
        res = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(res)
                res = 0
            else:
                res = stack.pop() + max(2 * res, 1)
            i += 1
        return res

-----------OR-----------
       if s.count('(')==s.count(')'):
            return s.count(')')
