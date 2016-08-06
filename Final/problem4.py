def getSublists(L, n):
    return [L[i:i+n] for i in range(len(L)-n+1)]


def longestRun(L):
    master = []
    longest = 0
    for i in range(len(L)+1):
        for k in getSublists(L, i):
            master.append(k)
    for h in master:
        if sorted(h) == h and len(h) >= longest:
            longest = len(h)
    return longest


print longestRun([1, 2, 3, -1, -2, -3, -4, -5, -6])