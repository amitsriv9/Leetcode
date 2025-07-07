import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        _temp = ''
        for _, char in enumerate(s):
            if re.match('[a-zA-Z0-9]', char) != None:
                _temp += char.lower()
        print(_temp)
        return self.checkPalindrome(_temp) 

    def checkPalindrome(self, _str):
        isPalindrome  =True
        if len(_str)>1:
            i, j = 0, len(_str)-1    
            while i<j:
                if _str[i] == _str[j]:
                    i+=1
                    j-=1
                else: 
                    isPalindrome = False
                    break
        return isPalindrome 


import unittest
class Tests(unittest.TestCase):
    def tetscase_one(self):
        pass
if __name__=='__main__':
    unittest.main()