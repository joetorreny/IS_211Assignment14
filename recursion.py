def fibonnaci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonnaci(n-1) + fibonnaci(n-2)


def gcd(a, b):
    smaller = min(a, b)
    bigger = max(a, b)
    if b == 0:
        return a
    return gcd(smaller, bigger % smaller)


def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    if len(s1) == 0:
        return -1
    if len(s2) == 0:
        return 1
    if s1[0] < s2[0]:
        return -1
    if s1[0] > s2[0]:
        return 1
    return compareTo(s1[1:], s2[1:])
