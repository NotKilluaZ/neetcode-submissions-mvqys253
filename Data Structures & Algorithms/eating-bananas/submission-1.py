class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        k = max_k

        while min_k <= max_k:
            mid = (max_k + min_k) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            if total_time > h:
                min_k = mid + 1
            else:
                k = mid
                max_k = mid - 1
        
        return k