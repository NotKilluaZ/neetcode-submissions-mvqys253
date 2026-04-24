class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = 1
        curr_min = 1

        for num in nums:
            if num == 0:
                curr_max = 1
                curr_min = 1
                continue
            
            temp = curr_max * num
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(temp, curr_min * num, num)

            res = max(curr_max, res)

        return res