class Solution:
    def search(self, nums: List[int], target: int) -> int:
      #can we rotat the array back to its starting position?
      # is there any way to run the algorithm with the rotated array.

        if target in nums:
            return nums.index(target)
        else:
            return -1