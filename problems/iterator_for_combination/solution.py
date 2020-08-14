class CombinationIterator:

    def __init__(self, c, l):
        self.n=len(c)
        self.c=c
        self.C=self.getCombinations(self.n,l)
        self.i=len(self.C)-1

    def next(self):
        b=self.C[self.i]
        s=""
        for i,v in enumerate(b):
            if v == "1":
                s+=self.c[i]
        self.i-=1
        return s
        

    def hasNext(self):
        return self.i >= 0
        
    def getCombinations(self, n, l):
        end=int("1"*n,2)
        ans=[]
        for x in range(end+1):
            b=bin(x)
            b=b[2:]
            if b.count("1") == l:
                ans.append(b.zfill(n))
        return ans



# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()