class TimeMap:

    def __init__(self):
        self.obj = {}


    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.obj:
            self.obj[key] = []
        self.obj[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.obj:
            return ""
        # find the appropriate timestamp
        #binsearch for prev timestamps
        start = 0
        end = len(self.obj[key])-1
        v = ""
        while(start<=end):
            mid = (start+end)//2
            if self.obj[key][mid][0]==timestamp:
                return self.obj[key][mid][1]
            if self.obj[key][mid][0]<timestamp:
                v = self.obj[key][mid][1]
                start = mid+1
            else:
                end = mid - 1
        return v
