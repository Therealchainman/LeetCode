class Solution:
    def calcEquation(self, E,V,Q):
        D={}
        i=0
        
        for x,y in E:
            if x not in D:
                D[x]=i
                i+=1
            if y not in D:
                D[y]=i
                i+=1
        n=len(E)
        graph=[[None]*(2*n) for _ in range(2*n)]
        
        for i,(x,y) in enumerate(E):
            graph[D[x]][D[y]]=V[i]
            graph[D[y]][D[x]]=1/V[i]
        m=len(D)
        # Floyd warshall's, but really I'm just going to compute the rest of the combinations.
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if graph[i][j] is None and graph[i][k] is not None and graph[k][j] is not None:
                        graph[i][j]=graph[i][k]*graph[k][j]

        ans=[]
        for x,y in Q:
            if  x not in D or y not in D:
                ans.append(-1)
                continue
            if graph[D[x]][D[y]] is None:
                ans.append(-1)
                continue
            ans.append(graph[D[x]][D[y]])
        return ans