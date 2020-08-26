class Solution:
    def fizzBuzz(self, n):
        str1="Fizz"
        str2="Buzz"
        ans=[]
        for d in range(1,n+1):
            if d%3==0 and d%5==0:
                ans.append(str1+str2)
            elif d%3==0:
                ans.append(str1)
            elif d%5==0:
                ans.append(str2)
            else:
                ans.append(str(d))
                
        return ans
        