class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        k = max_k

        while min_k <= max_k:
            m = (min_k + max_k) // 2
            total_time = 0
            for p in piles:
                time_req = math.ceil(p / m)
                total_time += time_req
            if total_time > h:
                min_k = m + 1
            else:
                max_k = m - 1
                k = m

        return k