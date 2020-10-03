from sortedcontainers import SortedList
import heapq
class Solution:
    def busiestServers(self, k,arrival,load):
        # This is a BST this way we can keep the available sorted so we can search through with binary search. 
        avail=SortedList(range(k))
        inf=float('inf')
        avail.add(inf)
        count=[0]*k
        # The heap will allow us to add servers that become newly available again back into available servers BST
        heap=[]
        
        def possible(val,target):
            return val>=target
        
        def binary_search(target,arr):
            lo,hi=0,len(arr)-1
            while lo<hi:
                mid=lo+hi>>1
                if not possible(arr[mid],target):
                    lo=mid+1
                else:
                    hi=mid
            return lo
        
        for idx,(a,l) in enumerate(zip(arrival,load)): 
            while heap and heap[0][0]<=a:
                _,index=heapq.heappop(heap)
                avail.add(index)
                
            n=len(avail)
            # There are no servers available right now
            if n==1:
                continue
            # The reason for mod with n is because if the binary search returns the last value in the avail.
            # We want to wrap around back to the first element in the available servers.
            avail_idx=binary_search(idx%k,avail)%(n-1)

            server_idx=avail[avail_idx]
            expiration_time=a+l
            heapq.heappush(heap,(expiration_time,server_idx))
            avail.remove(server_idx)
            count[server_idx]+=1
        ans=[]
        goal=max(count)
        for i,val in enumerate(count):
            if val==goal:
                ans.append(i)
        return ans
        
        
        