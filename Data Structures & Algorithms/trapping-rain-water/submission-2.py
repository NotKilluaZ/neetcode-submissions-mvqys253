class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        trapped_rain = 0
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(height[l], max_left)
                trapped_rain += max_left - height[l]
            else:
                r -= 1
                max_right = max(height[r], max_right)
                trapped_rain += max_right - height[r]

        return trapped_rain