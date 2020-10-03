
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans=[]
        D={}
        def convert(time):
            hours=time[:2]
            minutes=time[3:]
            return int(hours)*60+int(minutes)
        for i,time in enumerate(keyTime):
            keyTime[i]=convert(time)
        graph={}
        for index,name in enumerate(keyName):
            if name not in graph:
                graph[name]=[keyTime[index]]
            else:
                graph[name].append(keyTime[index])
        for part in graph.values():
            part.sort()
        for key,arr in graph.items():
            n=len(arr)
            for i in range(2,n):
                if arr[i] - arr[i-2]<=60:
                    ans.append(key)
                    break
        ans.sort()
        return ans
        