class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        min_heap = []
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for n, f in freq.items():
            heapq.heappush(min_heap, (f, n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        for f, n in min_heap:
            res.append(n)

        return res