from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        for index, row in enumerate(matrix):
            if self.searchRow(row, target):
                found = True
                break
        return found

    def searchRow(self, row, target):
        # if the row length is 2 or less to a normal lookup
        # else do binary search
        print(row)
        _length = len(row)
        if _length <= 2:
            if target in row:
                print('match found 2')
                return True
            else:
                print('not found')
                return False
        else:
            if target > row[_length//2]:
                if target < row[-1]:
                    return self.searchRow(row[_length//2:], target)
                else:
                    print('not found')
                    return False
            elif target < row[_length//2]:
                if target > row[0]:
                    return self.searchRow(row[0:_length//2], target)
                else:
                    print('not found')
                    return False
            else:
                print('match found 1')
                return True 

import unittest
class Tests(unittest.TestCase):
    def testcaseOne(self):
        obj = Solution()
        result = obj.searchMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 9)
        print(">>",result)

    def testcaseTwo(self):
        obj = Solution()
        result = obj.searchRow([1,2,3,4,5,6,7,8], 6)
        print(">>",result)

if __name__=='__main__':
    print("--00--")
    unittest.main()
