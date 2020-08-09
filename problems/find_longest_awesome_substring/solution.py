class Solution:
    def longestAwesome(self, S):
        prefix={}
        mask=0
        prefix[mask]=-1
        best=0
        for i,c in enumerate(S):
            x=int(c)
            mask ^=(1<<x)
            # If this state existed prior then that means we just canceled a bunch of numbers that appeared even number
            # times and resulted in a state that existed prior this is probably a combination of digits that all
            # appear even number times. 
            if mask in prefix:
                best=max(i-prefix[mask],best)
            else:
                prefix[mask]=i
            # Checking any number that appears odd number times and basically seeing if we have a previous
            # state that exist in the prefix dictionary.  If it does we want to use that because we can 
            # always permit one odd number in the palindrome.
            for k in range(10):
                findOdd=mask^(1<<k)
                if findOdd in prefix:
                    best=max(i-prefix[findOdd],best)

        return best
        