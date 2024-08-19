######################################################

#   Solved on Wednesday, 11 - 15 - 2023.

######################################################


######################################################

#   Runtime: 547ms   -   96.82%
#   Memory: 74.58MB  -   41.78%

######################################################

class TimeMap:

    def __init__(self):
        # timeMap structure:
        #   Key - key passed by user
        #   Value - List of [value, timestamp] passed by user
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap: self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # If key is not timeMap, we return empty string
        if key not in self.timeMap: return ""
        # Getting map for that key
        mapForKey = self.timeMap[key]
        # Since, timestamps are already in sorted order according to question,
        # if time stamp of first entry > given time stamp, we can't find 
        # a value with <= timestamp. So, we return ""
        if mapForKey[0][1] > timestamp: return ""
        # If time stamp of last entry <= given time stamp, that is the latest
        # value. So we return it
        if mapForKey[-1][1] <= timestamp: return mapForKey[-1][0]
        # Binary Search
        left = 0
        right = len(mapForKey) - 1
        while left <= right:
            mid = (left + right) // 2
            if mapForKey[mid][1] == timestamp: return mapForKey[mid][0]
            elif mapForKey[mid][1] > timestamp: right = mid - 1
            else: left = mid + 1
        return mapForKey[right][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)