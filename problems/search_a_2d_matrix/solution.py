class Solution:
    def searchMatrix(self, M,target):
        if not M:
            return False
        if not M[0]:
            return False
        
        R,C=len(M),len(M[0])
        
        def row_by_row(r,target):
            return M[r][0]<=target
        
        def target_in_row(r,c,target):
            return M[r][c]>=target
        
        def binary_search_row():
            lo,hi=0,R-1
            while lo < hi:
                mid=lo+hi+1>>1
                if row_by_row(mid,target):
                    lo=mid
                else:
                    hi=mid-1
            return lo
        
        def binary_search_in_row(row):
            lo,hi=0,C-1
            while lo < hi:
                mid=lo+hi>>1
                if not target_in_row(row,mid,target):
                    lo=mid+1
                else:
                    hi=mid
            return M[row][lo]
        
        row=binary_search_row()
        cand_val=binary_search_in_row(row)
        return target==cand_val
                    
            
        
"""
binary search row by row
TFF return last the occurrence of T. 

found the row tha tyo ushould search
binary search a row
FTTT return the first occurrence of T. 
TFFF
"""
        