class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        R,C=len(matrix),len(matrix[0])
        def possible(val,target):
            return val<=target
        
        def binary_search_row():
            lo,hi=0,R-1
            while lo<hi:
                mid=lo+hi+1>>1
                if possible(matrix[mid][0],target):
                    lo=mid
                else:
                    hi=mid-1
            return lo
        
        def binary_search_col(row):
            lo,hi=0,C-1
            while lo<hi:
                mid=lo+hi+1>>1
                if possible(matrix[row][mid],target):
                    lo=mid
                else:
                    hi=mid-1
            return lo
        
        x=binary_search_row()
        y=binary_search_col(x)
        return matrix[x][y]==target