class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = [0] * 26
        freq_t = [0] * 26

        for c in s:
            freq_s[ord(c) - ord("a")] += 1

        for c in t:
            freq_t[ord(c) - ord("a")] += 1

        if freq_s == freq_t:
            return True
        
        return False