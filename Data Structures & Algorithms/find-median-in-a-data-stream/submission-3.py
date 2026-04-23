class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, num * -1)

        if len(self.minheap) > len(self.maxheap) + 1:
            temp = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, temp * -1)
        if len(self.minheap) + 1 < len(self.maxheap):
            temp = heapq.heappop(self.maxheap) * -1
            heapq.heappush(self.minheap, temp)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        if len(self.minheap) < len(self.maxheap):
            return self.maxheap[0] * -1
        else:
            return (self.minheap[0] + (self.maxheap[0] * -1)) / 2
        