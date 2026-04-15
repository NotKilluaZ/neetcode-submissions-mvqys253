class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_paren = ["{", "(", "["]

        for para in s:
            if para in open_paren:
                stack.append(para)
            else:
                if len(stack) == 0:
                    return False
                if para == "}" and stack.pop() != "{":
                    return False
                if para == "]" and stack.pop() != "[":
                    return False
                if para == ")" and stack.pop() != "(":
                    return False

        if len(stack) != 0:
            return False

        return True