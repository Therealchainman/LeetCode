class Solution:
    def canPlaceFlowers(self, flowerbed,n):
        m=len(flowerbed)
        if m==1:
            return True if (flowerbed[0]!=1 and n==1) or n==0 else False
        for i,f in enumerate(flowerbed):
            if n==0:
                break
            if i==0:
                if f==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
            elif i==m-1:
                if f==0 and flowerbed[i-1]==0:
                    flowerbed[i]=1
                    n-=1
            else:
                if f==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
        return True if n==0 else False
        