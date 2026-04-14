class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            seperator = len(word)
            res  = res + str(seperator) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            str_len = ""
            i = 0
            while s[i] != "#":
                str_len = str_len + s[i]
                i += 1
            str_len = int(str_len)
            s = s[i + 1 : ]
            res.append(s[0 : str_len])
            s = s[str_len : ]

        return res
