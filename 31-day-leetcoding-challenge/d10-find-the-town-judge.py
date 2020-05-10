"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusters = set()
        s = 0
        for pair in trust:
            trusters.add(pair[0])
        
        town_judge_candidate = N*(N+1)//2 - sum(trusters)
        town_judge_trusters = set()
        
        for pair in trust:
            if pair[1] == town_judge_candidate:
                town_judge_trusters.add(pair[0])
        if len(town_judge_trusters) == len(trusters):
            return town_judge_candidate
        return -1