class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Pass 1: left-to-right. result[i] = product of everything LEFT of i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Pass 2: right-to-left. multiply in product of everything RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result