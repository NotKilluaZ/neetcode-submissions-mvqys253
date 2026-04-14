class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []
        open_par = {"(", "[", "{"}
        for para in s:
            if para in open_par:
                stack.append(para)
            elif len(stack) == 0:
                return False
            elif para == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif para == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            elif para == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
        if len(stack) != 0:
            return False

        return True