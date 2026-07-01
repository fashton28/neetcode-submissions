class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedList = sorted(nums)
        outputList = set()   # use set to avoid duplicates efficiently
        n = len(sortedList)

        for i in range(n):
            for j in range(i + 1, n):

                numberEquation = -(sortedList[i] + sortedList[j])

                # only search in remaining part
                if numberEquation in sortedList[j + 1:]:

                    # instead of index(), we avoid duplication entirely
                    triplet = tuple(sorted([
                        sortedList[i],
                        sortedList[j],
                        numberEquation
                    ]))

                    outputList.add(triplet)

        return [list(t) for t in outputList]