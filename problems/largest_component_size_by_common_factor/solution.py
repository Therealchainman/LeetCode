import math
from collections import defaultdict
class DSU:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size=[1]*(n+1)
        
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x!=y:
            if self.size[y]>self.size[x]:
                x,y=y,x
            # Assume node x is part of a larger connected component of nodes.
            # so set the parent of y to x so that the smaller is attached to larger
            self.size[x]+=self.size[y]
            self.size[y]=self.size[x]
            self.parent[y]=x
            
        
class Solution:
    def largestComponentSize(self,A):
        def prime_factors(n):
            primes=set()
            while n%2==0:
                primes.add(2)
                n//=2

            for i in range(3,int(math.sqrt(n))+1,2):

                while n%i==0:
                    primes.add(i)
                    n//=i

            if n>2:
                primes.add(n)

            return primes
        idx_list={A[i]:i for i in range(len(A))}
        dsu=DSU(len(A))
        prime_factor_map=defaultdict(list)
        for num in A:
            factors=prime_factors(num)
            for f in factors:
                prime_factor_map[f].append(num)
        for prime,multiples in prime_factor_map.items():
            root=multiples[0]
            for node in multiples[1:]:
                dsu.union(idx_list[root],idx_list[node])
        
        return max(dsu.size)
        
        