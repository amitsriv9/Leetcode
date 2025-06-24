from typing import List
START=0
END=1
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        self.meetingRooms = {}
        self.parseMeetings(intervals)
        return len(self.meetingRooms)
        
    def parseMeetings(self, intervals):
        for index, interval in enumerate(intervals):
            overlap = False
            print("interval :", interval)
            if len(self.meetingRooms) > 0:
                for key, value in self.meetingRooms.items():
                    last_meeting = value[-1]
                    # check overlap
                    if last_meeting[START] < interval[START] < last_meeting[END]:
                        overlap = True
                        continue
                    elif last_meeting[START] < interval[END] < last_meeting[END]:
                        overlap = True
                        continue
                    elif last_meeting[END] < interval[START]:
                        print("meeting room being Reused")
                        value.append(interval)
                        break
                    else:
                        pass
                if overlap:
                    _key = len(self.meetingRooms)+1
                    print("new meeting room being added ", _key)
                    self.meetingRooms[_key] = [interval]

            else:
                # empty dictionary
                print("first meeting room being added")
                self.meetingRooms[1] = [interval]

import unittest
class Tests(unittest.TestCase):
    def testone(self):
        obj = Solution()
        meetingRooms = obj.minMeetingRooms([[0,10], [12,15], [16,20], [21,25]])
        self.assertEqual(meetingRooms, 1)

    def testtwo(self):
        obj = Solution()
        meetingRooms = obj.minMeetingRooms([[0,10], [6,15], [16,20]])
        self.assertEqual(meetingRooms, 2)

if __name__=='__main__':
    unittest.main()
