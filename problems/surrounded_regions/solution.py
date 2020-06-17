class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return board
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and board[i][j] == "O":
                    self.dfs(i, j, board)
                elif i == n - 1 and board[i][j] == "O":
                    self.dfs(i, j, board)
                elif j == 0 and board[i][j] == "O":
                    self.dfs(i, j, board)
                elif j == m - 1 and board[i][j] == "O":
                    self.dfs(i, j, board)
        
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "R":
                    board[i][j] = "O"
        
    def dfs(self, i, j, board):
        if board[i][j] == "O":
            board[i][j] = "R"
        n = len(board)
        m = len(board[0])
        # Checking the position vertically above
        if i > 0 and board[i - 1][j] == "O":
            self.dfs(i - 1, j, board)
        # Checking the position vertically below
        if i < n - 1 and board[i + 1][j] == "O":
            self.dfs(i + 1, j, board)
        # Checking the position horizontally to the left
        if j > 0 and board[i][j - 1] == "O":
            self.dfs(i, j - 1, board)
        # Checking the position horizontally to the right
        if j < m - 1 and board[i][j + 1] == "O":
            self.dfs(i, j + 1, board)
        
"""
Start time: 3:02AM
approach1: 
1) look at all the O on the border and convert them to some random character like R.
2) if you find an O on the border do a dfs search for every O connected to that and change them to R.
3) Then convert all O to X
4) Then turn all R into O
5) return the board. 



"""