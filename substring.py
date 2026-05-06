from collections import Counter
def minWindow(s, p):
    d = Counter(p)
    n = len(s)
    res = ""
    for i in range(n):
        c = d.copy()
        for j in range(i, n):
            if s[j] in c:
                c[s[j]] -= 1
                if c[s[j]] == 0:
                    del c[s[j]]
            if not c:
                if res == "" or (j - i + 1) < len(res):
                    res = s[i:j+1]
                break
    return res
print(minWindow("timetopractice", "toc"))
