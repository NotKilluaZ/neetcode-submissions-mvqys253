class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        if len(nums) == 0 | len(nums) == 1:
            return output

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            output.append(prod)
        return output
