class Solution:
    def uniquePathsIII(self, A):
        R, C = len(A), len(A[0])
        count = 0
        # First objective is to count the number of empty cells that we must travel to in the grid.
        for r, c in product(range(R), range(C)):
            if A[r][c] == 0:
                count += 1
            elif A[r][c] == 1:  # mark -1 because cannot travel back to the start.
                sr, sc = (r, c)
                A[r][c] = -1
            elif A[r][c] == 2:
                fr, fc = (r, c)
                A[r][c] = 0  # I need to make the cell available for later and also count it as an empty cell needed to travel to.
                count += 1
        self.ans=0

        def dfs(r, c, res=0):
            # if we traverse all empty cells and are at the finish increment the answer.
            if (r, c, res) == (fr, fc, count):
                self.ans += 1
                return
            # Search in every possible direction as long as it is empty and in range.
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                    res += 1
                    A[nr][nc] = -1 # We don't want to travel to this again so mark it as obstacle.
                    dfs(nr, nc, res)
                    # This is the backtrack portion, after travelling to a cell we need to travel back
                    # so mark the cell as empty and decrement the number of cells we've traversed.
                    A[nr][nc] = 0
                    res -= 1

        dfs(sr, sc)
        return self.ans
        