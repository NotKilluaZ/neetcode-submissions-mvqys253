class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            size = str(len(s))
            res += size + "." + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            i = 0
            size = ""
            while s[i] != ".":
                size += s[i]
                i += 1

            size = int(size)
            s = s[i + 1: ]

            word = ""
            for j in range(size):
                word += s[j]

            res.append(word)
            s = s[size : ]

        return res