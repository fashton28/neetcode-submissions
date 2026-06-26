import math #importing math module. Think about how we could achieve this without the functions avaiable.

#any way to replicate the algorithm?

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Initial thoughts, work with position of current pointer position && length of list
        #Let me think of the least optimal solution first
        

        #The least optimal solution would be to brute force it by iterating ver the
        #Prefix and sufix technique.

        result = []
        for i in range(len(nums)):
            prefix_product = math.prod(nums[:i])     
            sufix_product  = math.prod(nums[i+1:])   
            result.append(prefix_product*sufix_product)
        return result

