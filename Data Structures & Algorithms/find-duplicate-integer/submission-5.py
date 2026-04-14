class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                nums[i] *= -1
            else:
                return abs(num)
        return -1