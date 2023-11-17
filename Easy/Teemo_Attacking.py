class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # first attempt: try to solve it linearly using math
        # add duration onto current time, if nextime is less than currenttime + duration that means
        # we reset so total time poisoned it nextime - currenttime + duration, otherwise it will be just duration
        if len(timeSeries) <= 1:
            return duration * len(timeSeries)

        totalDuration = 0
        i = 1
        while i < len(timeSeries):
            if timeSeries[i-1] + duration > timeSeries[i]:
                totalDuration += timeSeries[i] - timeSeries[i-1]
            else:
                totalDuration+=duration

            i+=1

        return totalDuration + duration # add duration for the last index