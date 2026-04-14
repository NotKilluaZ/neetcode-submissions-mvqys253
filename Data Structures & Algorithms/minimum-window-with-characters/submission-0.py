class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        res = ""
        count_t = {}
        window = {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        have = 0
        need = len(count_t)
        res = [-1, -1]
        res_len = float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l = res[0]
        r = res[1]
        if res_len == float("infinity"):
            return ""
        else:
            return s[l : r + 1]