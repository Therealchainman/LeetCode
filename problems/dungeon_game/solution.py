class Solution:
    def calculateMinimumHP(self, dungeon):
        n, m = len(dungeon), len(dungeon[0])
        arr = [[float('inf')]*(m + 1) for _ in range(n + 1)]
        arr[n - 1][m] = 1
        arr[n][m - 1] = 1
        for i in range(n-1, -1,-1):
            for j in range(m-1, -1,-1):
                arr[i][j] = max(min(arr[i + 1][j], arr[i][j + 1]) - dungeon[i][j], 1)
        
        return arr[0][0]
        

        
"""
Start time: 5:03PM
approach1:  
1) Compute the minimum health for the knight at each square. 

1) Right, Down, those are the two directions you can chooose.  
2) 

[[-2,-3,3],
[-5,-10,1],
[30,10,-20]]

[[(-2,-2), (-5,-5), (-5,-2)]
[(-7,-7), (-5,-5), (-5, -1)]
[(-7,23), (-5, 5), (-15,-15)]]

[[(-2,-2), (-5,-5), (-5,-2)]
[(-7,-7), (-5,-5), (-5, -1)]
[(-7,23), (-7,33), (-7,13)]]

1) reach the end of the path, reach the square where the princess is at.  
2) return -20
memo[i][j] = (dungeon[i][j], max(dungeon[i][j])

[[x,x,x],
[x,x,(-19,-20)],
[x,(10,-20),(-20,-20]]

-20, 
-21
-25

-17


Lowest hp along that path.  

1) Recursion pattern


"""