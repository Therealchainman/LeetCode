from collections import defaultdict
class DSU:
    def __init__(self,n):
        self.par=list(range(n))
        self.sz=[1]*n
    def find(self,x):
        if x!=self.par[x]:
            self.par[x]=self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        xr,yr=self.find(x),self.find(y)
        if xr!=yr:
            if self.sz[yr]>self.sz[xr]:
                xr,yr=yr,xr
            self.par[yr]=xr
            self.sz[xr]+=self.sz[yr]
            self.sz[yr]=self.sz[xr]
            return True
        return False
class Solution:
    def minCostConnectPoints(self, P):
        edges=[]
        manhattan=lambda p1,p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        for i,p in enumerate(P):
            x,y=p[0],p[1]
            for j in range(i+1,len(P)):
                u,v=P[j][0],P[j][1]
                man_dist=manhattan(p,P[j])
                edges.append((i,j,man_dist))
                edges.append((j,i,man_dist))
        dsu=DSU(len(P))
        edges.sort(key=lambda x: -x[2])
        total=0
        while edges:
            i,j,w=edges.pop()
            if dsu.union(i,j):
                total+=w
        return total
            
                

        