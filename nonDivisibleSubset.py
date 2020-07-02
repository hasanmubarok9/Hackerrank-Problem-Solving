def nonDivisibleSubset(k, S):

    print("S : ", S)
    d = {x:[] for x in range(k)}
    print("d : ", d)
    for i in range(len(S)): 
        print("S[i] : ", S[i])
        print("S[i]%k : ", S[i]%k)
        d[S[i]%k].append(S[i])
        print("d[S[i]%k] : ", d[S[i]%k])
    count = 0

    print("d : ", d)
    print("d[0] : ", d[0])
    if len(d[0]) > 0:
        count = 1

    arr = set([(x,k-x) for x in range(1,k//2+1)])
    print("arr : ", arr)

    print("d : ", d)
    for i,j in arr:
        print("i : ", i)
        print("j : ", j)
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1

        print("count : ", count)
    
    return count

print(nonDivisibleSubset(4, [19, 10, 12, 10, 24, 25, 22 ]))