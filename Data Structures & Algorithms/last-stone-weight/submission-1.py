class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            stone_one = heapq.heappop(max_heap)
            stone_two  = heapq.heappop(max_heap)
            if abs(stone_one) > abs(stone_two):
                heapq.heappush(max_heap, stone_one - stone_two)

        return abs(max_heap[0]) if max_heap else 0
            