from collections import OrderedDict
class LRUCache:
    # the end of the dictionary is the most recent
    # the beginning of the dictionary is the least recent
    def __init__(self, capacity: int):
        self.D = OrderedDict()
        self.cap=capacity

    def get(self, key: int) -> int:
        # if the key is already present, then move it to the end of dictionary
        if key in self.D:
            self.D.move_to_end(key,last=True)
            return self.D[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        # if the key is already present when you put it, then just move it to the end again
        # if over capacity pop the item that is at the beginning. 
        if key in self.D:
            self.D.move_to_end(key,last=True)
            self.D[key]=value
        elif len(self.D)==self.cap:
            self.D.popitem(last=False)
            self.D[key]=value
        else:
            self.D[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)