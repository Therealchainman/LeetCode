class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = set()
        cycleLen = 0
        cycle = False
        def nextDay(cells):
            temp = [0]*len(cells)
            for i in range(1, len(cells) - 1):
                temp[i] = 1 if cells[i-1] == cells[i+1] else 0
            return temp

        for i in range(N):
            nextCells= nextDay(cells)
            key = tuple(nextCells)
            if key in seen:
                cycle = True
                break
            seen.add(key)
            cycleLen += 1
            cells = nextCells
        if cycle:
            return self.prisonAfterNDays(cells, N % cycleLen)
        return cells