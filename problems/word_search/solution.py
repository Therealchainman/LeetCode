from collections import deque
class Solution:
    def exist(self, board, word):
        R, C = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word):
                return True
            
            for nr, nc in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    if board[nr][nc] == word[k] and (nr, nc) not in s:
                        visited.append((nr, nc))
                        s.add((nr, nc))
                        if dfs(nr, nc, k + 1):
                            return True
                        s.remove(visited.pop())
            return False

            
            
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    visited = [(r,c)]
                    s = {(r,c)}
                    if dfs(r, c, 1):
                        return True
                    visited = []
                    s.clear()
        return False
                

"""
[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
"ABCESEEEFS"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCB"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"SEE"
[["a","a"]]
"aaa"
[["C","A","A"],["A","A","A"],["B","C","D"]]
"AAB"


            visited[i][j] = True
            stack = list([(i, j, 1, visited)])
            while stack:
                r, c, k, visited = stack.pop()
                print(stack)
                print(k, word[k-1], visited)
                if k == len(word):
                    return True
                travel = False
                for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0 <= nr < R and 0 <= nc < C:
                        if board[nr][nc] == word[k] and not visited[nr][nc]:
                            visited[nr][nc] = True
                            travel = True
                            stack.append((nr, nc, k + 1, visited))
                if not travel:
                    visited[r][c] = False
                
            return False
"""