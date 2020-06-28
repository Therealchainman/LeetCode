class Solution:
    def isPathCrossing(self, s):
        coords = (0,0)
        count = {coords: 1}
        
        for x in s:
            if x == "S":
                coords = (coords[0], coords[1] - 1)
            elif x == "W":
                coords = (coords[0] -1, coords[1])
            elif x == "N":
                coords = (coords[0], coords[1] + 1)
            else:
                coords = (coords[0]+1, coords[1])
            if coords in count:
                return True
            count[coords] = 1
        return False              