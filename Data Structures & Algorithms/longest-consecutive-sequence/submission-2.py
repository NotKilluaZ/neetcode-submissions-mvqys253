class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
            
        nums_set = set()
        res = 1
        for i in range(len(nums)):
            nums_set.add(nums[i])

        for num in nums:
            if num - 1 in nums_set:
                continue
            
            seq = 1
            has_next = True
            i = 1

            while has_next:
                if num + i in nums_set:
                    seq += 1
                    i += 1
                else:
                    has_next = False


            if seq > res:
                res = seq
        
        return res