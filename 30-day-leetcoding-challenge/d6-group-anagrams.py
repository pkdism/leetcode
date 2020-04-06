"""Print groups of anagrams"""


class Solution:
    
    def check_anagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        hash1, hash2 = [0]*26, [0]*26
        ord_a = ord('a')
        n = len(str1)
        for i in range(n):
            hash1[ord(str1[i]) - ord_a] += 1
            hash2[ord(str2[i]) - ord_a] += 1
        
        for i in range(26):
            if hash1[i] != hash2[i]:
                return False
        return True
    
    def groupAnagrams(self, strs):
        n = len(strs)
        flag = [0]*n
        groups = []
        i = 0
        while i < n:
            while i < n and flag[i] == 1:
                i += 1
            j = i + 1
            cur_group = []
            if i < n:
                cur_group.append(strs[i])
                flag[i] = 1
            while j < n:
                if i < n and flag[j] == 0:
                    if len(strs[i]) == len(strs[j]):
                        if self.check_anagram(strs[i], strs[j]) == True:
                            flag[j] = 1
                            cur_group.append(strs[j])
                j += 1
            if cur_group != []:
                groups.append(cur_group)
        return groups

