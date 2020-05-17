class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        s = [set(x) for x in favoriteCompanies]
        n = len(favoriteCompanies)
        for i in range(n):
            isNotSubset = True
            for j in range(n):
                if i == j: 
                    continue
                if s[i].issubset(s[j]):
                    isNotSubset = False
            if isNotSubset:
                res.append(i)
        return res
                
        