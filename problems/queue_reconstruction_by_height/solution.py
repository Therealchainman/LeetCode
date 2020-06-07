class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = [[x,y,y] for x, y in people]
        
        out = []
        while people:
            ind = people.index(min(people,key=lambda x: (x[2],x[0])))
            out.append(people.pop(ind))
            people = [[x,y,z - (x <= out[-1][0])] for x,y,z in people ]
    
        return [[x,y] for x,y,z in out]