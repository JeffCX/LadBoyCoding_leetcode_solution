from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.array = []
        self.hashmap = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashmap:
            index = len(self.array)
            self.array.append(val)
            self.hashmap[val] = index
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashmap:
            index = self.hashmap[val]
            last_element = self.array[-1]
            self.array[index] = last_element
            self.hashmap[last_element] = index
            del self.hashmap[val]
            self.array.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()