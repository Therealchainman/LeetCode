class Solution:
    def sequentialDigits(self, low, high):
        A = []
        # Generate all satisfactory integers that follow the rule.
        
        def helper2(digit,k,num):
            if k==-1:
                return num
            return helper2(digit+1,k-1,num+digit*pow(10,k))
        
        def helper(j):
            nonlocal A
            for i in range(1,10-j):
                cand_val=helper2(i,j,0)
                if low<=cand_val<=high:
                    A.append(cand_val)
                    
        for j in range(1,10):
            helper(j)

        return A