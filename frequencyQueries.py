from collections import defaultdict

def freqQuery(data):
    d = defaultdict(int); f = defaultdict(set)
    for a, b in data:
        if a == 3: yield 1 if f[b] else 0; continue 
    
        f[d[b]].discard(b)
        if a == 1: d[b] += 1
        elif d[b] > 0: d[b] -= 1
        f[d[b]].add(b)

        print("d ", d)
        print("f ", f)













# def freqQuery(queries):

#     d = defaultdict(int) ; f = defaultdict(set)

#     for (c,v) in queries:
#         if c==3 : yield 1 if f[v] else 0 ; continue

#         f[d[v]].discard(v)
#         if c==1 : d[v] += 1
#         elif d[v]>0 : d[v] -= 1
#         f[d[v]].add(v)

for result in freqQuery([(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]):
    print(result)

