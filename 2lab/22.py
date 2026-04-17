class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = [("", 0, 0)]
        while stack:
            current_s, left, right = stack.pop()
            if len(current_s) == 2 * n:
                res.append(current_s)
                continue
            if left < n:
                stack.append((current_s + "(", left + 1, right))
            if right < left:
                stack.append((current_s + ")", left, right + 1))
        
        return res
if __name__ == "__main__":
    sol = Solution()
    n = 3
    result = sol.generateParenthesis(n)
    
    print(f"Для n={n}:")
    for combo in result:
        print(f" - {combo}")
    
    print(f"\nКомбинаций: {len(result)}")