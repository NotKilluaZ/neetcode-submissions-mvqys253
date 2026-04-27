class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = collections.defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)

        q = deque()
        seen = set()
        q.append(beginWord)
        seen.add(beginWord)

        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)

            res += 1

        return 0