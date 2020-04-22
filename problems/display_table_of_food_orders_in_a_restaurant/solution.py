class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        res = [["Table"]]
        tables = set()
        foodsy = set()
        dic = dict()
        for i in range(len(orders)):
            foodsy.add(orders[i][2])
        foodsy= sorted(list(foodsy))
        res[0] += foodsy
        for i in range(len(orders)):
            tables.add(int(orders[i][1]))
        tables = sorted(list(tables))
        tables = [str(tables[i]) for i in range(len(tables))]
        for t in tables:
            dic[t] = dict()
            for f in foodsy:
                dic[t][f] = 0
        for i in range(len(orders)):
            dic[orders[i][1]][orders[i][2]] += 1
        for t in tables: 
            for f in foodsy:
                dic[t][f] = str(dic[t][f])
        for t in tables:
            temp = [t]
            for f in foodsy:
                temp += dic[t][f]
            res += [temp]
        return res