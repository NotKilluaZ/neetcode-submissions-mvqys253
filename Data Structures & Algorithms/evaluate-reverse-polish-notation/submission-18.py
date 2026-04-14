class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(int(stack[-2]) + int(stack[-1]))
                stack.pop(-2)
                stack.pop(-2)
            elif token == "-":
                stack.append(int(stack[-2]) - int(stack[-1]))
                stack.pop(-2)
                stack.pop(-2)
            elif token == "*":
                stack.append(int(stack[-2]) * int(stack[-1]))
                stack.pop(-2)
                stack.pop(-2)
            elif token == "/":
                stack.append(int(int(stack[-2]) / int(stack[-1])))
                stack.pop(-2)
                stack.pop(-2)
            else:
                stack.append(token)

        return int(stack[0])