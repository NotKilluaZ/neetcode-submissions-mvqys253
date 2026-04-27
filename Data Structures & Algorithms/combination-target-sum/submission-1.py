class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        curr_sum = 0

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            if curr_sum > target or i >= len(nums):
                return

            curr.append(nums[i])
            curr_sum += nums[i]
            dfs(i, curr, curr_sum)
            curr_sum -= curr.pop()
            dfs(i + 1, curr, curr_sum)

        dfs(0, curr, curr_sum)
        return res