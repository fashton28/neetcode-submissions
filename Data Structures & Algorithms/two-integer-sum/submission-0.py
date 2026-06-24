class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #trivial solution --> Create two for loops, add conditional and return indices.
        #Optimal solution --> Creating hashmap
        #Now, we must think, how do we create a hashmap and how do we build it optimally so that it's easy to manipulate and access it.
        #Why hashmaps --> used for O(1) look-ups


        #[1,2,3,4,5] target = 4
        createHash = {}
    
        finalList = []

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in createHash:
                finalList.append(createHash[difference])
                finalList.append(i)
                return finalList
            else:
                createHash[nums[i]] = i