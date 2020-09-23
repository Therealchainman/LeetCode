class Solution:
    def canCompleteCircuit(self, G,C):
        n=len(G)
        sum_gas=sum_cost=tank=start=0
        for i in range(n):
            sum_gas+=G[i]
            sum_cost+=C[i]
            tank+=G[i]-C[i]
            if tank<0:
                start=i+1
                tank=0
        return start if sum_gas>=sum_cost else -1
        