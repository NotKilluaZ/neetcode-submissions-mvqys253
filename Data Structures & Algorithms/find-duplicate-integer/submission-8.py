class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            i = abs(i)
            if nums[i - 1] < 0:
                return i
            else:
                nums[i - 1] *= -1

        return -1