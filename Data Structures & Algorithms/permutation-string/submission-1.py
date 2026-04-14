class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        for c in s1:
            target[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if target == window:
            return True

        for r in range(len(s1), len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            left_char = s2[r - len(s1)]
            window[ord(left_char) - ord('a')] -= 1

            if target == window:
                return True

        return False