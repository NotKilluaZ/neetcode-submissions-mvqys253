class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(curr.copy())  
                return

            if self.isPalindrome(s, j, i):
                curr.append(s[j:i+1])
                dfs(i + 1, i + 1)
                curr.pop()

            dfs(j, i + 1)

        dfs(0, 0)
        return res

    def isPalindrome(self, word, j, i) -> bool:
        l = j
        r = i

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

        