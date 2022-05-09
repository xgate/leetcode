class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ')' and top != '(':
                    return False
                if c == ']' and top != '[':
                    return False
                if c == '}' and top != '{':
                    return False
        
        if stack:
            return False
        
        return True
