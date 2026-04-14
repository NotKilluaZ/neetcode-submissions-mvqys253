class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = -1
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            max_height = min(heights[l], heights[r])
            max_area = max(max_area, max_height * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area