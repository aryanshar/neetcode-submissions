class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.min_arr):
            top_min = self.min_arr[-1]
            curr_min = min(val, top_min)
            self.min_arr.append(curr_min)
        else:
            self.min_arr.append(val)

    def pop(self) -> None:
        if len(self.min_arr):
            self.min_arr.pop()
        if len(self.arr):
            return self.arr.pop()
        return None

    def top(self) -> int:
        if len(self.arr):
            return self.arr[-1]
        return None

    def getMin(self) -> int:
        if len(self.min_arr):
            return self.min_arr[-1]
        return None