class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        sortedArray = sorted(nums)
        return sortedArray[0]