"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
Thus, the itinerary must begin with JFK.
"""


class Solution:
    
    def dfs(self, place):
        while self.dic[place]:
            airport = self.dic[place].pop()
            self.dfs(airport)
        self.path.append(place)
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.path = []
        self.dic = defaultdict(list)
        
        for source, dest in tickets:
            self.dic[source].append(dest)
            
        for source, dest in tickets:
            self.dic[source] = sorted(self.dic[source], reverse = True)
        
        self.dfs("JFK")
        return self.path[::-1]