class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            one = 0
            two = 0

            for n in nums:
                temp = max(one + n, two)
                one = two
                two = temp

            return two

        return max(nums[0], rob_helper(nums[1:]), rob_helper(nums[:-1]))