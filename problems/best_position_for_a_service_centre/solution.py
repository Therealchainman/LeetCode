import math
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def euclideanDist(p1, p2):
	        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        def sumED(p, points):
	        return sum(euclideanDist(p, q) for q in points)

        def arithmeticMean(points):
            n = len(points)
            xm, ym = (sum(x for x, _ in points) / n, sum(y for _, y in points) / n)
            return xm , ym

        def simulatedAnnealing(arr):
            dirs = [(-1,0), (1,0), (0,-1), (0,1)]
            INF = float('inf')
            n = len(arr)
            cx, cy = arithmeticMean(arr)
            step, limit = 10, 1e-6
            minDist = sumED([cx, cy], arr)
            while step > limit:
                improved = False
                for xd, yd in dirs:
                    nx, ny = cx + step*xd, cy + step*yd
                    ndist = sumED([nx, ny], arr)
                    if ndist < minDist:
                        improved = True
                        cx, cy = nx, ny
                        minDist = ndist
                if not improved:
                    step /= 2
            return minDist
        return simulatedAnnealing(positions)
    
"""
approach1:  Use scipy.optimize.minimize
x0 = [0,0]
func = lambda p: sum(math.sqrt((p[0] - x)**2 + (p[1] - y)**2) for x, y in positions)
res = minimize(func,x0)
return res.fun

approach2: gradient descent

"""