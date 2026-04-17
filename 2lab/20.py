class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in pair:
                top = stack.pop() if stack else '#'
                if pair[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack
sol = Solution()

print(sol.isValid("()[]{}"))
print(sol.isValid("(]")) 