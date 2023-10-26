from collections import deque


def hashword(word):
    h = 0
    c = 1
    for i in word:
        h += c * (ord(i) - 97)
        c = c * 26
    return h


def unhash(value, length):
    c = 1
    word = []
    for i in range(length):
        cr = chr(((value % (c * 26)) // c) + 97)
        word.append(cr)
        c = c * 26
    return "".join(word)


class Solution:
    def findladders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = {}
        for i in range(len(wordList)):
            d[hashword(wordList[i])] = 0
        h = hashword(beginWord)
        q = deque()
        q.append(h)
        f = hashword(endWord)
        q = deque()
        q.append([h, 1])
        d[h] = 1
        main_ans = []
        s = 1
        while q:
            x = q.popleft()
            h = x[0]
            if h == f:
                s = x[1]
                break
            else:
                c = 1
                for i in range(len(beginWord)):
                    for j in range(26):
                        y = h - (((h % (c * 26)) // c) * c) + (c * j)
                        if y in d:
                            if d[y] == 0:
                                d[y] = x[1] + 1
                                q.append([y, x[1] + 1])
                    c = c * 26
        ans = deque()
        if f in d:
            if d[f] == s:
                ans.append([f])
                while len(ans[0]) < s:
                    x = ans.popleft()
                    h = [-1]
                    c = 1
                    for i in range(len(beginWord)):
                        for j in range(26):
                            y = h - (((h % (c * 26)) // c) * c) + (c * j)
                            if y in d:
                                if d[y] == s - len(x):
                                    x.append(y)
                                    ans.append(x[::])
                                    x.pop()
                        c = c * 26
        a = []
        while ans:
            x = ans.popleft()
            ab = []
            while x:
                k = unhash(x.pop(), len(beginWord))
                ab.append(k)
            a.append(ab)
        return a

