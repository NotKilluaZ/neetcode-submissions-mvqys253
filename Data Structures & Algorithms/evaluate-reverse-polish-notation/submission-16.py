class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                second_operand = int(stack[-1])
                first_operand = int(stack[-2])
                stack.pop()
                stack.pop()
                operator = token
                expression = f"{first_operand} {operator} {second_operand}"
                ans = eval(expression)
                stack.append(ans)
        
        return int(stack[-1])