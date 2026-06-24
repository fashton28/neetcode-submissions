class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #BUCKET SORT
        #notes
        #Most optimal solution takes bucket sort approach
        # the index becomes our reference for the frequency.
        #So we just need to create an array that groups all elements that correspond to that frequency and return it
        #Now, we also need to do so from top to bottom, returning those elements with greater frequency first, until we get to k
        #Also, in order to know counts we need to create hashmap to know that per element
        #Nice problem, as it combines a variety of concepts.

        count = {}
        freq = [[] for i in range(len(nums)+1)] 

        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i,c in count.items():
            freq[c].append(i)

        result = []
        for j in range(len(freq)  - 1, 0, -1):
            for n in freq[j]:
                result.append(n)
                if len(result) ==k:
                    return result
         
        # a heap would've given us a slightly less efficient solution.


            
    




            
            