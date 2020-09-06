class DSU:
    def __init__(self,n):
        """
        Args:
            n(int): The number of nodes or vertices in the graph.
        """
        # n+1 because using 1-indexing for the node values so node values are from 1,2...,n, creat array [0,1,...,n]
        self.par=list(range(n+1))
        self.size=[1]*(n+1)
        
    def find(self,x):
        if x!=self.par[x]:
            self.par[x]=self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        xp=self.find(x)
        yp=self.find(y)
        if xp!=yp:
            if self.size[xp]<self.size[yp]:
                xp,yp=yp,xp
            self.par[yp]=xp
            self.size[xp]+=self.size[yp]
            self.size[yp]=self.size[xp]
            return True
        return False
    
    def get_size(self,x):
        return self.size[self.par[x]]
        
class Solution:
    def maxNumEdgesToRemove(self, n,edges):
        dsuA=DSU(n)
        dsuB=DSU(n)
        ans=0
        for t,x,y in edges:
            if t==3:
                if not dsuA.union(x,y):
                    ans+=1
                dsuB.union(x,y)
        for t,x,y in edges:
            if t==1:
                if not dsuA.union(x,y):
                    ans+=1
            elif t==2:
                if not dsuB.union(x,y):
                    ans+=1
        return ans if dsuA.get_size(1)==dsuB.get_size(1)==n else -1
        