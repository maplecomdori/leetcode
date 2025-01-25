class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        min_val = float('inf')
        adj_lst = defaultdict(set) # edge between words if they differ by one

        def is_diff_by_one(first, second):
            count = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    count += 1
                if count > 1:
                    return False
            return count == 1

        # build edge between beginWord and words in wordList
        for word in wordList:
            if is_diff_by_one(beginWord, word):
                adj_lst[beginWord].add(word)
                # adj_lst[word].add(beginWord)

        # build edge among words in wordList
        for i in range(len(wordList) - 1):
            first = wordList[i]
            for j in range(i+1, len(wordList)):
                second = wordList[j]
                if is_diff_by_one(first, second):
                    adj_lst[first].add(second)
                    adj_lst[second].add(first)

        # bfs
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        distance = 0

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance + 1

                for nei in adj_lst[word]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            distance += 1

        return 0
'''
hit => cog, using [hot dot dog lot log cog]

hit: hot

hot: dot, lot
dot: dog, hot
dog: dot, log, cog
lot: hot, dot, log
log: dog, lot, cog
cog: log, dog, 

'''