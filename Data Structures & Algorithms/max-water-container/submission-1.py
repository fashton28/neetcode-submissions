class Solution:
    def maxArea(self, heights: List[int]) -> int:        

        #define my right and left pointers

        area = 0
        l,r = 0, len(heights) - 1

        while l < r:
            currentDistance = r - l
            if heights[r] < heights[l]:
                currentHeight = heights[r]
            else:
                currentHeight = heights[l]

            prospectiveArea = currentDistance * currentHeight

            if area < prospectiveArea:
                area = prospectiveArea

           #determine the strategy to move pointers
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return area