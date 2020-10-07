class LLNode:
    def __init__(self,key,val,next=None):
        self.p=(key,val)
        self.next=next
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m=2531
        self.h=[None]*self.m
        

    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        """
        i=key%self.m
        cur=self.h[i]
        if cur==None:
            self.h[i]=LLNode(key,val)
            return
        while cur:
            if cur.p[0]==key:
                cur.p=(key,val)
                return
            if cur.next==None:
                break
            cur=cur.next
        cur.next=LLNode(key,val)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i=key%self.m
        cur=self.h[i]
        while cur:
            if cur.p[0]==key:
                return cur.p[1]
            cur=cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i=key%self.m
        prev=cur=self.h[i]
        if cur==None:
            return
        if cur.p[0]==key:
            self.h[i]=cur.next
            return
        cur=cur.next
        while cur:
            if cur.p[0]==key:
                prev.next=cur.next
                return
            prev=prev.next
            cur=cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)