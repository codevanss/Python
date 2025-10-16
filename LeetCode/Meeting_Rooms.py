# Definition of Interval.
class Interval(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda i : i.start)

        for i in range(1 , len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True

intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
Solution().canAttendMeetings(intervals)
