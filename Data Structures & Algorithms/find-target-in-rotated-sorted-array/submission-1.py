class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = ((right - left) // 2) + left
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return - 1


        l = 0
        r = len(nums) - 1

        while l < r:
            m = ((r - l) // 2) + l
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        res = binary_search(0, l - 1)
        if res != -1:
            return res
        res = binary_search(l, len(nums) - 1)

        return res