class TimeMap:

    def __init__(self):
        self.dict = defaultdict(dict)
        self.recentDict = defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.dict[key].update( {timestamp:value})
        self.recentDict[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict:
            if timestamp in self.dict[key]:
                return self.dict[key][timestamp]
            # find the most recent timestamp thats before the given timestamp
            maxVal = self.recentDict[key][len(self.recentDict[key]) - 1]
            minVal = self.recentDict[key][0]
            if timestamp > maxVal:
                return self.dict[key][maxVal]
            if timestamp < minVal:
                return ""
            # we need to find a timestamp less than it
            tempList = self.recentDict[key]
            for i in range(len(tempList)):
                if tempList[i] > timestamp:
                    return self.dict[key][tempList[i-1]]
            return self.dict[key][self.recentDict[key][0]]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)