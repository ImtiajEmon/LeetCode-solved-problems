class SmallestInfiniteSet:

    def __init__(self):
        self.set = [1]
        

    def popSmallest(self) -> int:
        MIN = min(self.set)
        if len(self.set) > 1 and MIN != self.set[0]:
            self.set.remove(MIN)
            return MIN
        else:
            self.set[0] += 1
            return  self.set[0]-1

        

    def addBack(self, num: int) -> None:
        if num < self.set[0] and num not in self.set:
            self.set.append(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
