from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr, self.map = [], {}
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.arr:
            self.arr.append(val)
            index = len(self.arr) - 1
            self.map[val] = index
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.arr:
            index, lastVal = self.map[val], self.arr[-1]
            self.arr[index], self.arr[-1] = lastVal, self.arr[index]
            self.map[lastVal] = index
            self.arr.pop()
            self.map.pop(val)
            return True
        return False
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)
        
"""
Start time: 3:55PM
approach1:  list
insert -> O(1)
remove -> O(n)
getRandom -> O(1)

approach2: hashmap
insert -> O(1)
remove -> O(1)
getRandom -> O(n)

approach3: hashmap + list
insert -> O(1)
remove -> O(1)
getRandom -> O(1)


arr = [2,5,1,7,9]
map = {2: 0, 5: 1, 1: 2, 7: 3, 9: 4}
map (key, val) -> (element value, index in the array)


What about remove.   
RemovedSet.remove(1)
[2,5,1,7,9] -> [2,5,9,7,1] -> [2,5,9,7]
update the hashmap -> {2:0}

The only way to have O(1) removal from a list is to remove from the end that is to use pop() on the last element. 
map.remove(key)

Why is it O(1) in getRandom, well just use the array which you can index in. and use random.choice(arr)




"""

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()