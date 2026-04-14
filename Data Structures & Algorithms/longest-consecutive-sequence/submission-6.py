class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq = 0

        for n in nums:
            if n - 1 not in nums:
                seq = 1
                while n + seq in nums:
                    seq += 1

                longest_seq = max(longest_seq, seq)

        return longest_seq