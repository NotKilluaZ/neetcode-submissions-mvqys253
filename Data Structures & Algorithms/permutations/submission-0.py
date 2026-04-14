class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, curr: List[int], nums: List[int], picked: List[bool]):
        if len(curr) == len(nums):
            self.res.append(curr.copy())
            return

        for i in range(len(nums)):
            if not picked[i]:
                curr.append(nums[i])
                picked[i] = True
                self.backtrack(curr, nums, picked)
                curr.pop()
                picked[i] = False
