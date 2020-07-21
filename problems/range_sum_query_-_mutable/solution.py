class NumArray:

    def __init__(self, num):
        self.arr = num
        self.bit = [0] + num
        for i in range(1, len(self.bit)):
            j = i + (i & -i)
            if j < len(self.bit):
                self.bit[j] += self.bit[i]
        

    def update(self, i, val):
        inc = val - self.arr[i]
        self.arr[i] = val
        i += 1
        while i < len(self.bit):
            self.bit[i] += inc
            i += (i & -i)
            
    def prefixSum(self, i):
        res = 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res
    
    def sumRange(self, i, j):
        return self.prefixSum(j + 1) - self.prefixSum(i)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

"""
start time: 6:46PM
approach1: prefix sum array

def __init__(self, num):
    if not num:
        return
    n = len(num)
    self.arr = num
    self.prefixArr = [0]*n
    self.prefixArr[0] = self.arr[0]
    for i in range(1, n):
        self.prefixArr[i] = self.prefixArr[i-1] + self.arr[i]

def update(self, i, val):
    self.arr[i] = val
    self.prefixArr[0] = self.arr[0]
    n = len(self.arr)
    for i in range(1, n):
        self.prefixArr[i] = self.arr[i] + self.prefixArr[i-1]


def sumRange(self, i, j):
    if i == 0:
        return self.prefixArr[j]
    if i == j:
        return self.arr[i]
    return self.prefixArr[j] - self.prefixArr[i - 1]


approach2:  Fenwick tree (BIT)




"""