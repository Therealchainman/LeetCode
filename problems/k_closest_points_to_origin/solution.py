import random
class Solution:
    def kClosest(self,points,K):
        ## Approach : Random quick sort partitioning (O(n))
        if K == len(points) :
            return points
        dist = lambda p: p[0]**2 + p[1]**2
        compare = lambda p1,p2 : dist(p1) - dist(p2)

        def partition(start, end) :
            p = random.randint(start,end) 
            points[p] ,points[start] = points[start],points[p] # Swap pivot with right most ele
            l, r  = start , end
            while True:
                while l < r and  compare(points[r], points[start]) >= 0 :
                    r -= 1
                while l < r and compare(points[l] , points[start]) <= 0:
                    l += 1
                if  l<r :
                    points[l] , points[r] = points[r], points[l]
                else :
                    break
            points[start], points[r] = points[r] , points[start]
            return r

        i, j = 0 , len(points) -1
        while i <= j:
            pivot = partition(i,j)
            if pivot  ==  K-1 :
                return points[:K]
            elif pivot < K -1 :
                i = pivot + 1
            else :
                j = pivot - 1
        
        