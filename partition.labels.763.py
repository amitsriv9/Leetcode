from typing import List


'''
scna the string once 
create a dictionary and not indices for the alphebets

if the string is bigger than 2 ie 3
look for the three characters on the other side
choose the middle of the list
scan all elements on one side and create dict on the other side  

aa bb cc dd
abab cdcd
abcdabcd
'''
class Solution:
    def __init__(self):
        self.charmap = {}
    
    def partitionLabels(self, s: str) -> List[int]:
        for index, char in enumerate(s):
            if self.charmap.get(char, None) is None:
                self.charmap[char] = [index]
            else:
                self.charmap[char].append(index)
        print(self.charmap)
        # self.getPartition(s)
        # print(self.partitions)
        return 

    def getPartition(self, s):
        print("inside ispartition valid")
        self.partitions = []
        index = 0
        while True:
            char = s[index]
            start = index
            occurance = self.charmap[char]
            end = max(occurance)
            _end = self.isPartitionValid(s, start, end)
            if _end != -1:
                self.partitions.append((start, _end))
            # next partition
            if _end+1 < len(s):
                index = _end+1
            else:
                break

    def isPartitionValid(self, s, start, end):
        print("inside ispartition valid", start, end)
        nextEnd = -1
        for _, item in enumerate(s[start:end]):
            temp = max(self.charmap[item])
            if temp > end:
                if temp > nextEnd:
                    nextEnd = temp
        return nextEnd

import unittest
class Tests(unittest.TestCase):
    def testcaseOne(self):
        obj = Solution()
        s = "aabbccdd"
        obj.partitionLabels(s)

if __name__=='__main__':
    unittest.main() 