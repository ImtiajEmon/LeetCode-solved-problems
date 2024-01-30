class RecentCounter:

    def __init__(self):
        self.lst = list()
        

    def ping(self, t: int) -> int:
        self.lst.append(t)
        start = t - 3000

        for i in range(len(self.lst)):
            if self.lst[i] >= start:
                break

        return len(self.lst) - i
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
