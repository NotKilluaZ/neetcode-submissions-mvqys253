class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}

        for num in nums:
            count[num] = 0

        for num in nums:
            count[num] += 1
        
        # Key: integer  ||   Value: freq

        count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

        for i in range(k):
            first = next(iter(count))
            res.append(first)
            count.pop(first)

        return res