class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        for i in range(len(self.arr)):
            if num <= self.arr[i]:
                self.arr.insert(i, num)
                return
        self.arr.append(num)

    def findMedian(self) -> float:
        return statistics.median(self.arr)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
