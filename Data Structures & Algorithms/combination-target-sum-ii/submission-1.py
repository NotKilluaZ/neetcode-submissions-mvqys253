class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
        curr_sum = 0
        i = 0

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or curr_sum > target:
                return
            
            curr.append(candidates[i])
            curr_sum += candidates[i]
            dfs(i + 1, curr, curr_sum)

            curr_sum -=curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, curr, curr_sum)


        dfs(0, curr, curr_sum)
        return res