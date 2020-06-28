from collections import deque
class Solution:
    def findMaxValueOfEquation(self, p: List[List[int]], k: int) -> int:
        ans = float('-inf')
        i = 0
        q = deque()
        for x, y in p:
            val = y - x
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                ans = max(ans, q[0][0] + x +y)
            while q and q[-1][0] <= val:
                q.pop()
            q.append([val, x])
        return ans
            
"""
So why does this work?  

Hello, let's do code analysis over this solution.  
Why does it work. 

Let's analyze what each component means

We begin by getting the x, y values from the points
Now initially the queue is empty
We are going to use an invariant that is it will be a monotonic queue.

So we don't do anything.  We only append to the queue the current value which is y -x,  
Think about why that is important because we always add the negative of the previous x value
According to the fact that xj>xi while j > i.  Also we keep track of the previous x value as well.
We go to the next element and compute its value.  
Now there is something important.  
We wish to move the sliwind window in the sene that if any of the first appearing values that is like where the left pointer is pointing
if the current x minus that previous x is greater than k, what should we do.  Will obviously we don't care about that previous q
So we remove that value.  

Now there is a crucial fact we need to learn about this deque.  
Notice that at the end we have this bizarre process of basically popping from q the last elemtns then appending our current val, and x
Why is this.  
Will let's analyze when it does this removing of the last elem. Suppose the very last val in our queue is smaller than our current value.
What does that mean.  That means some previous y-x is smaller than current y - x,  now realize that since we always add x and y. 
We don't care about thos smaller y-x because we only want a max queue here.  So we pop those smaller values.  If there is val that is greater
we stop and just add new element right there. 

Now you see that when you popleft you are just removing elements that you cannot use in the answer because no 
longer satisfy condition.  Until you get to the first elemtn you can use
You know this will giv you the max value and basically you then will go to the bottom and remove anything else you don't need because current value is too high.

1) Remove from the front of the deque if the xi does not satisfy the condition xj-xi<=k
2) if we still have a queue update your current max value by taking the front part of the queue.
3) the reason that works is because this is a monotonically decreasing queue.  or minqueue.
4)  We keep it a minqueue by doing the following.  We remove the end of the elements if they appear to have a smaller value
5) reason is because they won't matter this new element is going to last the longest, because x is strictly increasing.
6) in addition by doing this you make sure it is the maxqueue.  So highest value is at the front of the queue.
7) then you continue to next round and see if you have a new max.  
"""
    