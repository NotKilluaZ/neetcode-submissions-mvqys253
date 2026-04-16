class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(l, r):
            while l <= r:
                m = (r + l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

            return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        target_indx = bin_search(0, l)
        if target_indx != -1:
            return target_indx
        else:
            return bin_search(l, len(nums) - 1)