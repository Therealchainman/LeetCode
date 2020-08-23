class Solution:
    def findLatestStep(self,A,m):
        n=len(A)
        length=[0]*(n+2)
        count=[0]*(n+1)
        ans=-1
        for i,a in enumerate(A):
            left,right=length[a-1],length[a+1]
            length[a]=length[a-left]=length[a+right]=left+right+1
            count[left]-=1
            count[right]-=1
            count[length[a]]+=1
            if count[m]>0:
                ans=i+1
        return ans


"""
start time: 5:05am
approach2:  A not necessarily obvious solution but works because it update the count appropriately and we update the length of each
group appropriately be keeping track at the outer edges, and we look at those two surrounding values when we insert a new one into a group
Then when we insert it into a group we basically just add its left and right side length values +1 to get the new value and then update the left and right borders as well with this new group size thus communicating it to any potential adjacent nodes to it later on. 
"""
