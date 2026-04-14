class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            max_height = heights[i]
            for j in range(i, len(heights)):
                if heights[j] < max_height:
                    max_height = heights[j]
                area = (j - i + 1) * max_height
                areas.append(area)

        return max(areas)