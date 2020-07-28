"""
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. 
Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.
You need to return the least number of units of times that the CPU will take to finish all the given tasks.
"""


from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        dic = Counter(tasks)
        most = dic.most_common()[0][1]
        res = sum([dic[key] == most for key in dic])
        return max(len(tasks), (most - 1) * (n + 1) + res)