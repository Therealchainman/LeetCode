from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        stack, backtrack = ["JFK"], []
        airportMap = defaultdict(list)
        for dep, arr in sorted(tickets, reverse=True):
            airportMap[dep].append(arr)
        while stack:
            dep = stack[-1]
            while airportMap[dep]:
                stack.append(airportMap[dep][-1])
                airportMap[dep].pop()
                dep = stack[-1]
            stack.pop()
            backtrack.append(dep)
        return backtrack[::-1]
            
            
        
        
        
    
"""

"""
        