class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append((price, 1))
            return 1

        cnt = 1
        while True and len(self.stack) > 0:
            if self.stack[-1][0] <= price:
                cnt += self.stack[-1][1]
                self.stack.pop()
            else:
                break
        self.stack.append((price, cnt))

        return cnt
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
