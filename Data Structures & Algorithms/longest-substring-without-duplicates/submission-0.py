class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        newset = set() 
        newlist = list(s)
        longest = 0
        account = []
        left = 0
        for i in range(len(newlist)):
            while newlist[i] in newset:
                newset.remove(newlist[left])
                left += 1
            newset.add(newlist[i])
            longest = i - left + 1
            account.append(longest)
                
        return max(account)
