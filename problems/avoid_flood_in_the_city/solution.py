from collections import defaultdict
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        lakes, lastRain = set(), defaultdict(int)
        dry = []
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i)
                res.append(1)
                continue
            res.append(-1)
            if lake in lakes:
                if not dry:
                    return []
                index = lastRain[lake]
                lastRain[lake] = i
                found = False
                for j, d in enumerate(dry):
                    if d > index:
                        res[d] = lake
                        dry.pop(j)
                        found = True
                        break
                if not found:
                    return []
            else:
                lakes.add(lake)
                lastRain[lake] = i
        return res