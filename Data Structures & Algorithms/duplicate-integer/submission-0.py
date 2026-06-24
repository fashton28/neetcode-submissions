class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        createSet = set()
        array = nums
        for i in array:
            if i not in createSet:
                createSet.add(i)
            else:
                return True
        return False