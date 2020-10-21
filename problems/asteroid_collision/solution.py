class Solution:
    def asteroidCollision(self, asteroids):
        if not asteroids:
            return []
        stk=[asteroids[0]]
        for ast in asteroids[1:]:
            stk.append(ast)
            if len(stk)<2:
                continue
            while len(stk)>1 and stk[-2]>=0 and stk[-1]<0:
                y=stk.pop()
                x=stk.pop()
                if x>abs(y):
                    stk.append(x)
                    break
                elif x==abs(y):
                    break
                else:
                    stk.append(y) 
        return stk