class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odds_sum = sum([v%2 for k, v in c.items()])
        if odds_sum <= 1:
            return len(s)
        else:
            return len(s) - odds_sum + 1