class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(int(a / b))
        return stack[0]
    
if __name__ == "__main__":
    sol = Solution()
    test1 = ["2", "1", "+", "3", "*"]
    print(f" {test1} => {sol.evalRPN(test1)} (верно 9)")
    test2 = ["4", "13", "5", "/", "+"]
    print(f" {test2} => {sol.evalRPN(test2)} (верно 6)")
    test3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(f"{test3} => {sol.evalRPN(test3)} (верно 22)")