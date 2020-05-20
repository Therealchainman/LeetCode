class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        res = 1
        while self.prices:
            prev, span = self.prices[-1]
            if price >= prev:
                res += span
                self.prices.pop()
            else:
                break
        self.prices.append((price, res))
        return res

"""
Start at 11:40PM
add prices to an array and then return the number of previous days with lower stocks.  
brute-force naive approach fails
so now I need to try a different approach that optimizes somehow perhaps?
[100, 80, 60, 70, 60, 75, 85]
Use a stack is the best way to solve this. 
so suppose
we get [(100, 1), (80, 1), (60, 1)]
but 70 is greater than the last element so now we need to increment by 1, and then it is less than 80 so we then need to 
add to stack [(100, 1), (80, 1), (70, 2)]
next value is 60 so it is smaller than the last value in stack so just do this
[(100, 1), (80, 1), (70, 2), (60, 1)]
next value is 75 and so it is larger and will pop two things from stack, and add the values each time to n 
so it gets [(100, 1), (80, 1), (75, 4))]
then we go to 85 and yeah that is larger so it will addthe 4 and 1 and its 1 to get 6. 
"""
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)