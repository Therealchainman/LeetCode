from collections import Counter
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, nums, res = 0, Counter(), 0
        for r in range(len(tree)):
            nums[tree[r]] += 1
            while len(nums) > 2:
                nums[tree[l]] -= 1
                if not nums[tree[l]]:
                    nums.pop(tree[l])
                l += 1
            res = max(res, r - l + 1)
        return res
            
    
'''
How to approach this problem, I know I will need to use the 2 steps, but what determines.  so on
So my approach is going to try to thinking through the problem and the main statements in theproblem and consider how to approach solving it with the most appropriate algorithm, and just coding it will be very nice.  
First thing I notice is that well,  it appears that we add one piece of fruit to my basket.  
First step is to figure out which tree I want to start collecting from.  Well the problem is that I don't know at first it would determine on once I have computed the number of fruits that I have collected.  But this depends on going through the problem.  
So it seems to me I need to create some thought process.  

So don't I want to start at each unique integer.  So for instance I should start collecting at a, and then if I reach integer b I should start another collection there.  But this might not be the best.  So there is a way to consider how this works.  
I need to somehow track all of the integers that I want to start from when computing.  So I could implement a data structure, and my favorite one to go to here is the double ended queue because I can remove from the front with time complexity O(1).  So this is cool.  

So I should have a queue that basically always adds to it unique numbers.  Totally awesome.  I hope that works lol.  The next step is to consider the idea that I need to create a way to basically count how many integers I can pass through.  

So for instance I could take [1,2,1] and I will be like I add 1 and 2 to my double ended queue.  and also this creats another conundrum because I don't want to add a duplicate, but uh how to do that with a queue?  Uh Oh this doesn't look good.  I am just struggling so much.  do not lose track of time it is 6pm currently.  The next thing that This sounds bad but I could have a set keeping track of what I have seen.  uh sure it will add to space complexity but should be okay to go with.  

Alright so the next step is going to be how am I going to deal with the overall concept.  So I need to keep track of the length of the collection but then once I reach a new integer, how do I know I've reached a new integer.  
I need to keep track of 
so I think I am out of time I need to start coding.  But yeah YOu can see where I am going with this.  I will need methods to keep track of certain things.  And I want to return the maximum
'''