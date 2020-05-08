class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = make_satisfied = l = will_satisfy = 0
        for r in range(len(customers)):
            satisfied += (1 - grumpy[r]) * customers[r]
            make_satisfied += grumpy[r] * customers[r]
            X -= 1
            if X <= 0:
                will_satisfy = max(make_satisfied, will_satisfy)
                make_satisfied -= grumpy[l] * customers[l]
                l += 1
        return satisfied + max(will_satisfy, make_satisfied)
        
'''
Start: 2:09pm
end: never what lol? 
'''