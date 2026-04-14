class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        max_k = max(piles)
        min_k = 1
        k = max_k

        while min_k <= max_k:
            m = ((max_k - min_k) // 2) + min_k
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / m)
            if total_time <= h:
                k = m
                max_k = m - 1
            else:
                min_k = m + 1

        return k