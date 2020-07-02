from collections import defaultdict

n, m = map(int, input().split())

A = defaultdict(list)
for i in range(n):
    a = str(input())
    A[a].append(i + 1)

B = []
for _ in range(m):
    b = str(input())
    B.append(b)

for el in B:
    if el in A:
        print(' '.join(map(str, A[el])))
    else:
        print(-1)
