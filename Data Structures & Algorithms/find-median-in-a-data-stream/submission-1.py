class MedianFinder:

    def __init__(self):
        self.rolling_list = []
        

    def addNum(self, num: int) -> None:
        self.rolling_list.append(num)

        

    def findMedian(self) -> float:
        count = len(self.rolling_list)
        self.rolling_list = sorted(self.rolling_list)
        if count % 2 == 0:
            mid1 = self.rolling_list[count//2 - 1]
            mid2 = self.rolling_list[count //2 ]
            return (mid1 +mid2) /2
        else:
            return self.rolling_list[count // 2]

        
        