from typing import List

class Solution:
    def __init__(self):
        self.merged = []
        self.visited = []

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for index, interval in enumerate(intervals):
            if interval not in self.merged:
                self.visited.append(interval)
                if len(intervals[index+1:]) > 0:
                    self.mergeIntervals(interval, intervals[index+1:])
        return self.visited

    def mergeIntervals(self, interval, intervals):
        print(f"interval {interval}, incoming list {intervals}")
        print(f"merged {self.merged}")
        merged = False
        for _, _interval in enumerate(intervals):
            if _interval not in self.merged:
                _x, _y = self.checkIntervals(interval, _interval)
                if _x is not None:
                    interval = [_x, _y]
                    print("merging happened", interval)
                    merged, mergeIndex = True, _
                    self.visited.pop()
                    self.visited.append(interval)
        if merged:
            for _, _interval in enumerate(intervals):
                if _ >= mergeIndex:
                    break
                if _interval not in self.merged:
                    _x, _y = self.checkIntervals(interval, _interval)
                    if _x is not None:
                        print(f">>{_x},{_y}")
                        interval = [_x, _y]
                        self.visited.pop()
                        self.visited.append(interval)
                        # print("merging happened", interval)

    def checkIntervals(self, interval1, interval2):
        # print("inside check intervals")
        x1,y1 = interval1
        x2,y2 = interval2
        
        x3,y3=None, None
        if x1 <= x2 <= y1 \
        or x2 <= x1 <= y2:
            print(f"going to merge{x1},{y1} & {x2},{y2}")
            self.merged.append(interval2)
            x3 = x1 if x1<x2 else x2
            y3 = y1 if y1>y2 else y2
        return x3,y3


import unittest
class Tests(unittest.TestCase):
    def testcaseOne(self):
        print("\n-1-")
        obj = Solution()
        x,y = obj.checkIntervals([1,4], [2,5])
        self.assertEqual([1,5], [x,y])
        print("\n")

    def testcaseTwo(self):
        print("\n-2-")
        obj = Solution()
        _response = obj.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
        self.assertEqual([[1,10]], _response)
        print("\n")
    
    def testcaseThree(self):
        print("\n-3-")
        obj = Solution()
        _response = obj.merge([[1,4],[0,4]])
        self.assertEqual([[0,4]], _response)
        print("\n")

if __name__=='__main__':
    unittest.main()