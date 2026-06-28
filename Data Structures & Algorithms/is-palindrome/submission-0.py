class Solution:
    def isPalindrome(self, s: str) -> bool:
        #write string with no whitespaces or uppercase.

        parsedString = ''
        for char in s:
            if char.isalnum():
                parsedString += char
        
        return parsedString.lower() == parsedString[::-1].lower()


        


