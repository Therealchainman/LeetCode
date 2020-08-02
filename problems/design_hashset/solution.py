class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        m = 10**6
        self.hashSet = [-1]*(m+1)

    def add(self, key: int) -> None:
        self.hashSet[key] = key

    def remove(self, key: int) -> None:
        self.hashSet[key] = -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hashSet[key] != -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)