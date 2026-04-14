class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        min_heap = []
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for n in freq.keys():
            heapq.heappush(min_heap, (freq[n], n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res