class Solution:
    def numsSameConsecDiff(self, N,K):
        A=range(10)
        for i in range(N-1):
            cur=set()
            for x in A:
                for y in [x%10+K,x%10-K]:
                    if x and 0<=y<10:
                        cur.add(x*10+y)
            A=cur
        return list(A)
                        
        #     A={x*10+y for x in A for y in [x%10+K,x%10-K] if 0<=y<10}
        # return list(A)