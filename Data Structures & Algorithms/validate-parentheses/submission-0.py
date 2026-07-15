class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')': '(', ']': '[', '}': '{'}   # closer -> opener
        stack = []

        for ch in s:
            if ch in pairs:                       # it's a closer
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:                                 # it's an opener
                stack.append(ch)

        return not stack