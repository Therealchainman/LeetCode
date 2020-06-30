from collections import defaultdict
from collections import deque
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, subBoards = defaultdict(set), defaultdict(set), defaultdict(set)
        emptyCells = deque()
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    ch = board[r][c]
                    rows[r].add(ch)
                    cols[c].add(ch)
                    subBoards[(r // 3, c // 3)].add(ch)
                else:
                    emptyCells.append((r,c))
        
        def dfs():
            if not emptyCells:
                return True
            r, c = emptyCells[0]
            t = (r // 3, c // 3)
            for n in [str(i) for i in range(1,10)]:
                if n not in rows[r] and n not in cols[c] and n not in subBoards[t]:
                    board[r][c] = n
                    rows[r].add(n)
                    cols[c].add(n)
                    subBoards[t].add(n)
                    emptyCells.popleft()
                    if dfs():
                        return True
                    rows[r].discard(n)
                    cols[c].discard(n)
                    subBoards[t].discard(n)
                    emptyCells.appendleft((r,c))
                    board[r][c] = "."
            return False
            
            
            
            
        dfs()
        
        
        
        
"""
Start time: 6:41PM
approach1: DFS + backtracking
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]


(0,2)
0%3 = 0, 2%3=2 row - row%3
OR
(3,4) -> 3 - 3%3 = 3, 4 - 4%3 = 3 -> (3,3)
so it belongs

"""