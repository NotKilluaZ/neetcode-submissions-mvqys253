class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            curr_height = min(heights[l], heights[r]) * (r - l)
            if curr_height > max_height:
                max_height = curr_height

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_height