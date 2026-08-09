class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 0
        while right <= len(nums) - 1 and left <= len(nums) - 1:
            if left != right and nums[left] == nums[right] and abs(left - right) <= k:
                return True
            elif right == len(nums) - 1:
                left += 1
                right = left
            else:
                right += 1
        
        return False

        
        #had to make sure we weren't checking the same index

      
        
