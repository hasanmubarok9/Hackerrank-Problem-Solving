from collections import Counter


def twoStrings(s1, s2):
    print(Counter(s1)-Counter(s2))
    if (Counter(s1)-Counter(s2)) == Counter(s1):
        return "NO"
    return "YES"


print(twoStrings('hello', 'world'))
print(twoStrings('hi', 'world'))
