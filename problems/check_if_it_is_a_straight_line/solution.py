class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = c[:2]
        return all((y2 - y1) * (x - x1) == (x2 - x1) * (y - y1) for x, y in c)