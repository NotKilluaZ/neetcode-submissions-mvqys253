class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        q = deque()
        seen = set()
        res = 1

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)

        q.append(beginWord)
        seen.add(beginWord)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in seen:
                            seen.add(neiWord)
                            q.append(neiWord)

            res += 1
        return 0