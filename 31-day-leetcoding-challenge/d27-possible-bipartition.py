"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.
"""


class Solution:
	def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
		
		if len(dislikes) == 0:
			return True
		
		if len(dislikes) == 1:
			return True
		
		g1, g2 = set(), set()
		
		first = dislikes.pop(0)

		g1.add(first[0])
		g2.add(first[1])
		
		l = len(dislikes)
		
		res = 0
		
		while len(dislikes) > 0:
			
			n1, n2 = dislikes.pop(0)
			
			if n1 not in g1 and n2 not in g1 and n1 not in g2 and n2 not in g2: 
				dislikes.append([n1, n2])
			elif n1 in g1:
				if n2 in g1:
					return False
				else:
					if n2 not in g2:
						g2.add(n2)
			elif n2 in g1:
				if n1 in g1:
					return False
				else:
					if n1 not in g2:
						g2.add(n1)
			elif n1 in g2:
				if n2 in g2:
					return False
				else:
					if n2 not in g1:
						g1.add(n2)
			elif n2 in g2:
				if n1 in g2:
					return False
				else:
					if n1 not in g1:
						g1.add(n1)
			# print(res)
			res += 1
			
			if res == l and len(g1) == 1 and len(g2) == 1:
				return False

		return True