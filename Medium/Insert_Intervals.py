class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find if the interval overlaps with anything
            # if none then just add the interval into the correct spot
        # add any overlapping intervals into a list
            # check start interval of the new interval first
            # check end interval of the new interval
        # any intervals that don't overlap, add them to res
        # check that the first interval added starts before the start time of the newinterval
            # change the start time to be new intervals
        # check that the last interval ends before the end time of the new interval
            # change end time to be new intervals
        
        if intervals == []:
            return [newInterval]

        res  = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)

        return res

        
