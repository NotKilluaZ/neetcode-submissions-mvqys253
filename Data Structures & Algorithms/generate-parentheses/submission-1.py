class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_para, para_avail, curr):
            if open_para == 0 and para_avail == 0:
                res.append(curr)
                return

            if para_avail > 0:
                backtrack(open_para + 1, para_avail - 1, curr + "(")

            if open_para > 0:
                backtrack(open_para - 1, para_avail, curr + ")")

        backtrack(0, n, "")
        return res