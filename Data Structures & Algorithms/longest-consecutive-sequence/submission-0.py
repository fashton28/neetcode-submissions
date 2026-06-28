class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   

        #so we essentially needed a way to find the actual longest!

        sortedList = sorted(set(nums)) #add set to remove duplicates
        longest = 1
        current = 1

        if len(nums) == 0:
            return 0

        for i in range(1,len(sortedList)):
            if sortedList[i] == sortedList[i-1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest,current)
              
        return longest