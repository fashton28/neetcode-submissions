class Solution:
    def isValid(self, s: str) -> bool:

     pairs = {")":"(", "}":"{", "]":"["}
     stack = []

     for e in s:
        if e in pairs:
            if not stack or stack.pop() != pairs[e]:
                return False
        else:
            stack.append(e)
    
     return not stack #where we determine the follwing: if it's empty then that means we matched all the elements we needed.






































       