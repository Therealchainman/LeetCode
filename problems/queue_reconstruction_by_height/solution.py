class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        q = []
        people = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
        for p in people:
            h, k = p
            if not q:
                q.append(p)
            else:
                q.insert(k, p)
        return q
        
"""
Start time: 10:08 PM
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

[[5,0], [], [5, 2], [], [4,4]]
"""