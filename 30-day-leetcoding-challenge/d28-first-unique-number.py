"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

    FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
    int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
    void add(int value) insert value to the queue.
"""


from collections import defaultdict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniques = []
        self.counts = defaultdict()
        for x in nums:
            self.add(x)
        
    def showFirstUnique(self) -> int:
        while len(self.uniques) > 0 and self.counts[self.uniques[0]] > 1:
            self.uniques.pop(0)
        if len(self.uniques) > 0:
            return self.uniques[0]
        else:
            return -1
                    
    def add(self, value: int) -> None:
        if value in self.counts:
            self.counts[value] += 1
        else:
            self.counts[value] = 1
            self.uniques.append(value)
        

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)