# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #number from 1 to n is picked
        #so, we're essentially given a target. 
        #and the number picked is embedded behind the logic of the guess api

        #if those two numbers match, then return the picked number
        # if guess is higher, then we move pointers.
        # ig guess is lower, we also move pointers.

        #this means first guess should start in the middle

        l,r = 1, n #we can do 1,n because we aren't working with an array

        while l <= r:
            mid = (l+r) // 2
            attempt = guess(mid)
            if attempt == - 1:
                r = mid -1
            elif attempt == 1:
                l = mid + 1
            else:
                return mid 

        


