from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, subs = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                dig = board[r][c]
                t = (r // 3, c // 3)
                if dig != ".":
                    if dig in rows[r] or dig in cols[c] or dig in subs[t]:
                        return False
                    rows[r].add(dig)
                    cols[c].add(dig)
                    subs[t].add(dig)
        return True
        
"""
Start time: 11:48PM
approach1: Hashing 
1) check each row contains no duplicates
2) check each col contains no duplicates
3) check each sub board does not contain any duplicates

Create a dictionary for each row
row maps to a set of the values contained in that row.
if every we see a value that is already in that row then we return False
rows = {0: {}, 1: {}}
Same thing for columns

Same thing for sub boards.  

(0,0),(0,1),(0,2)
(1,0),(1,1),(1,2)
(2,0),(2,1),(2,2)

r // 3 and c // 3


"""