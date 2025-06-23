from typing import List
'''
 0 1 2 3 4 5
 0 1 2 3 4 5 6
 ^         ^
 right right -index
       5 - 0
       5 - 1

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return
        length = len(s)
        temp, right = None, length-1
        
        for index, char in enumerate(s):
            if index == (length //2):
                break
            right = length - index -1
            
            temp = s[index]
            s[index] = s[right]
            s[right] = temp
            print(index, right)
        

