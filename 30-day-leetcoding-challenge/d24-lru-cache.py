from collections import defaultdict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = defaultdict()
        self.priority = defaultdict()
        self.p_value = 0
        self.lowest_value = 0
        
    def prnt(self):
        print("dictionary", self.dic)
        print("priority", self.priority)
        print("p_value", self.p_value)
        print("lowest_point", self.lowest_value)
        print("")

    def get(self, key: int) -> int:
        
        # print("Under get -------------------")
        # print("get key", key)
        
        if key in self.dic.keys():
            self.p_value += 1
            if self.p_value > self.capacity:
                self.lowest_value += 1
            self.priority[self.p_value] = key
            
            # print("Under if --------")
            # self.prnt()
            
            return self.dic[key]
        
        else:
            
            # print("Under else --------")
            # self.prnt()
            
            return -1

    def put(self, key: int, value: int) -> None:
        
        # print("Under put -------------------")
        # print("put key", key, " value", value)
        
        if key in self.dic.keys():
            self.capacity += 1
        
        self.dic[key] = value
        
        if self.p_value > self.capacity:
            
            self.lowest_value += 1
            x = self.dic.pop(self.priority[self.lowest_value])
            self.p_value += 1            
            self.priority[self.p_value] = key
            
            
            # print("Under if --------")
            # self.prnt()
            
        else:
            
            self.p_value += 1
            self.priority[self.p_value] = key
            
            # print("Under else --------")
            # self.prnt()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)