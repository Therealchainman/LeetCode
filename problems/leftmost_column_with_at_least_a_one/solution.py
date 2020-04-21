# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        nRows = binaryMatrix.dimensions()[0] - 1
        nCols = binaryMatrix.dimensions()[1] - 1
        r = 0
        c = nCols
        res = -1
        while c > -1 and r <= nRows:
            p = binaryMatrix.get(r, c)
            if p == 0:
                r += 1
            else:
                res = c
                c -= 1
        return res