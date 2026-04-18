class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        seen = set()
        q = deque()
        res = 1
        adj = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)

        q.append(beginWord)
        seen.add(beginWord)

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)

            res += 1

        return 0