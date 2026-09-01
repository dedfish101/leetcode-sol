class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        opening = ('(','[','{')
        closing = (')',']','}')
        q = []
        for c in s:
            if not q:#if empty
                q.append(c)
                continue
            if c in closing:
                if opening.index(q[-1]) == closing.index(c):
                
                    q.pop()
            if c in opening:
                q.append(c)
        

            

                

        return not q
